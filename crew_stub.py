class Agent:
    """Minimal stub of crewai.Agent used for testing."""

    def __init__(self, role: str, goal: str, llm: dict | str):
        self.role = role
        self.goal = goal
        self.llm = llm
