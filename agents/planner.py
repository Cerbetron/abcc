from crewai import Agent

planner = Agent(
    role="Planner",
    goal="Plan out steps",
    llm={"provider": "openai", "model": "gpt-4-turbo"}
)
