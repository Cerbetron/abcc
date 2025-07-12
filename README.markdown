# Agent Usage Tracker

This project provides a framework for running multiple OpenAI-powered agents, tracking their token usage, and visualizing the results in an interactive web dashboard.

## Features
- Run multiple agents defined in the `agents/` directory
- Track and log token usage for each agent
- Visualize token usage statistics through a FastAPI-powered web dashboard
- Downloadable CSV log of token usage data
- Customizable agent prompts and pricing data

## Requirements
- Python 3.10 or newer
- An OpenAI API key set as the environment variable `OPENAI_API_KEY`
- Required Python packages:
  ```bash
  pip install fastapi uvicorn pandas python-dotenv openai tiktoken
  ```

## Project Structure
- `agents/`: Contains agent scripts (`planner.py`, `reviewer.py`, `writer.py`)
- `logs/`: Stores token usage logs (`agent_usage_log.csv`)
- `pricing/`: Contains model token pricing data (`model_token_prices.csv`)
- `templates/`: HTML templates for the web dashboard
- `utils/`: Utility scripts, including `tracker.py` for token usage tracking
- `app.py`: FastAPI application for serving the dashboard
- `run_agents.py`: Script to execute agents and log token usage
- `.gitignore`: Git ignore file for excluding unnecessary files

## Setup
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd agent-usage-tracker
   ```
2. Set up a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install fastapi uvicorn pandas python-dotenv openai tiktoken
   ```
4. Set your OpenAI API key:
   ```bash
   export OPENAI_API_KEY='your-api-key'  # On Windows: set OPENAI_API_KEY=your-api-key
   ```

## Running the Agents
To execute the agents and log their token usage:
```bash
python run_agents.py
```
This script:
- Loads all agents from the `agents/` directory
- Runs each agent with a sample prompt
- Writes token usage statistics to `logs/agent_usage_log.csv`

## Viewing the Dashboard
To start the FastAPI web server and view the dashboard:
```bash
uvicorn app:app --reload
```
- Open your browser and navigate to `http://localhost:8000` to view the interactive dashboard.
- Download the token usage log at `http://localhost:8000/log.csv`.

## Customization
- **Modify Agents or Prompts**: Edit `run_agents.py` to change the sample prompt or add/remove agents from the `agents/` directory.
- **Update Pricing**: Modify `pricing/model_token_prices.csv` to reflect changes in OpenAI API pricing.
- **Extend Functionality**: Add new agents to the `agents/` directory or enhance the dashboard in `templates/`.

## Contributing
Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add your feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a pull request

## Author
- **Dinesh Kumar**
- **Arnav Gupta**

## License
This project is licensed under the MIT License.
