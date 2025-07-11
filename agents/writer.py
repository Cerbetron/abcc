from openai import OpenAI

class Writer:
    def __init__(self):
        self.model = "gpt-4"
        self.client = OpenAI()

    def run(self, prompt):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a writer drafting the final Mars mission plan."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()