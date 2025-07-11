"""Run all agents with a mock prompt and log token usage and costs."""
from __future__ import annotations

import importlib.util
import os
import sys
from dataclasses import dataclass

import pandas as pd

# provide a stub crewai module so agent definitions can be imported without
# the real package being installed
import types
from crew_stub import Agent as StubAgent

sys.modules.setdefault('crewai', types.ModuleType('crewai'))
setattr(sys.modules['crewai'], 'Agent', StubAgent)

PROMPT = "Plan a trip to Mars"
AGENT_DIR = "agents"
PRICING_FILE = os.path.join("pricing", "model_token_prices.csv")
LOG_FILE = os.path.join("logs", "agent_usage_log.csv")

@dataclass
class LoadedAgent:
    name: str
    obj: StubAgent


def load_agents() -> list[LoadedAgent]:
    agents: list[LoadedAgent] = []
    for file in os.listdir(AGENT_DIR):
        if not file.endswith(".py"):
            continue
        path = os.path.join(AGENT_DIR, file)
        module_name = os.path.splitext(file)[0]
        spec = importlib.util.spec_from_file_location(module_name, path)
        if spec and spec.loader:
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            agent_obj = getattr(module, module_name, None)
            if agent_obj:
                agents.append(LoadedAgent(module_name, agent_obj))
    return agents


def run_interactions() -> pd.DataFrame:
    pricing = pd.read_csv(PRICING_FILE).set_index("model_name")
    rows = []
    from utils.tracker import track_tokens

    for loaded in load_agents():
        agent = loaded.obj
        if isinstance(agent.llm, dict):
            model = agent.llm.get("model", "")
        else:
            model = str(agent.llm)

        # Mock the response. In a real scenario, this would invoke the agent.
        response = f"{agent.role} response to: {PROMPT}"

        input_tokens, output_tokens = track_tokens(PROMPT, response, model)
        prices = pricing.loc[model]
        cost = (input_tokens / 1000) * prices["input_price_per_1k"] + (
            output_tokens / 1000
        ) * prices["output_price_per_1k"]

        rows.append(
            {
                "agent_name": loaded.name,
                "model_used": model,
                "input_tokens": input_tokens,
                "output_tokens": output_tokens,
                "total_cost_usd": round(float(cost), 6),
            }
        )

    return pd.DataFrame(rows)


def main() -> None:
    df = run_interactions()
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    df.to_csv(LOG_FILE, index=False)
    print(df)


if __name__ == "__main__":
    main()
