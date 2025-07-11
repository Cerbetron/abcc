"""Utility script to summarise token usage logs."""
from __future__ import annotations

import pandas as pd


def analyze_costs() -> None:
    """Print token and cost totals grouped by agent."""

    df = pd.read_csv("logs/agent_usage_log.csv")
    pricing = pd.read_csv("pricing/model_token_prices.csv")
    merged = pd.merge(
        df,
        pricing,
        left_on="model_used",
        right_on="model_name",
        how="left",
    )
    merged["cost"] = (
        merged["input_tokens"] / 1000 * merged["input_price_per_1k"]
        + merged["output_tokens"] / 1000 * merged["output_price_per_1k"]
    )
    summary = merged.groupby("agent_name")[["input_tokens", "output_tokens", "cost"]].sum()
    print(summary)


if __name__ == "__main__":
    analyze_costs()
