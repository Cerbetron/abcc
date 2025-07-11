from crewai import Agent

writer = Agent(
    role="Writer",
    goal="Write content",
    llm={"provider": "openai", "model": "llama-3-8b"}
)
