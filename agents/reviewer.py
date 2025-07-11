from openai import OpenAI

class Reviewer:
    def __init__(self):
        self.model = "gpt-3.5-turbo"
        self.client = OpenAI()

    def run(self, prompt):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a mission reviewer and critique planner."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()