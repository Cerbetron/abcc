# Placeholder for script to analyze costs from logs
import pandas as pd

def analyze_costs():
    df = pd.read_csv('logs/agent_usage_log.csv')
    pricing = pd.read_csv('pricing/model_token_prices.csv')
    merged = pd.merge(df, pricing, on='model_name')
    merged['cost'] = (merged['input_tokens']/1000)*merged['input_price_per_1k'] + (merged['output_tokens']/1000)*merged['output_price_per_1k']
    summary = merged.groupby('agent_name')[['input_tokens','output_tokens','cost']].sum()
    print(summary)
