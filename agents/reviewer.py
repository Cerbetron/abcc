from crewai import Agent

reviewer = Agent(
    role="Reviewer",
    goal="Review the output",
    llm={"provider": "openai", "model": "gpt-3.5-turbo"}
)
