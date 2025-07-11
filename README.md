# Agent Usage Tracker

This project demonstrates a small framework for running multiple OpenAI powered agents, tracking their token usage and visualising the results in a web dashboard.

## Requirements

* Python 3.10 or newer
* An OpenAI API key available in the environment as `OPENAI_API_KEY`

Install the required packages:

```bash
pip install fastapi uvicorn pandas python-dotenv openai tiktoken
```

## Running the agents

Execute the pipeline defined in `run_agents.py`:

```bash
python run_agents.py
```

This script loads every agent in the `agents/` directory, runs them with a sample prompt and writes token usage statistics to `logs/agent_usage_log.csv`.

## Viewing the dashboard

Start the FastAPI application to serve the HTML report:

```bash
uvicorn app:app --reload
```

Navigate to `http://localhost:8000` to see the interactive dashboard. You can also download the CSV log at `http://localhost:8000/log.csv`.

## Customisation

* Edit `run_agents.py` to change the prompt or add/remove agents.
* Update `pricing/model_token_prices.csv` if the API pricing changes.

