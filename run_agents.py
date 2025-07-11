
"""Run all agents using OpenAI Chat API and log token usage and cost."""

import importlib.util
import os
from dataclasses import dataclass
from datetime import datetime
import pandas as pd
from dotenv import load_dotenv
from utils.tracker import track_tokens
import openai

# Load environment variables (for OPENAI_API_KEY)
load_dotenv()

PROMPT = "Plan a trip to Mars"
AGENT_DIR = "agents"
PRICING_FILE = os.path.join("pricing", "model_token_prices.csv")
LOG_FILE = os.path.join("logs", "agent_usage_log.csv")

@dataclass
class LoadedAgent:
    name: str
    obj: any
    model: str


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
            agent_class = getattr(module, module_name.capitalize(), None)
            if agent_class:
                agent_instance = agent_class()
                agents.append(LoadedAgent(module_name, agent_instance, agent_instance.model))
    return agents


def run_interactions() -> pd.DataFrame:
    pricing = pd.read_csv(PRICING_FILE).set_index("model_name")
    rows = []

    for loaded in load_agents():
        model = loaded.model
        agent = loaded.obj

        try:
            response = agent.run(PROMPT)
        except Exception as e:
            print(f"Error running agent '{loaded.name}': {e}")
            response = "ERROR"

        print(f"\n--- {loaded.name.upper()} RESPONSE ---")
        print(response)
        print("-------------------------------\n")

        input_tokens, output_tokens = track_tokens(PROMPT, response, model)

        try:
            prices = pricing.loc[model]
        except KeyError:
            print(f"Pricing not found for model: {model}")
            prices = {"input_price_per_1k": 0.0, "output_price_per_1k": 0.0}

        cost = (input_tokens / 1000) * prices["input_price_per_1k"] + (
            output_tokens / 1000
        ) * prices["output_price_per_1k"]

        rows.append(
            {
                "timestamp": datetime.now().isoformat(),
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
    print("\n=== COST SUMMARY ===")
    print(df[["agent_name", "model_used", "input_tokens", "output_tokens", "total_cost_usd"]])


if __name__ == "__main__":
    main()
