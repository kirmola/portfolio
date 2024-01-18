import requests
from os import environ


class GenerateResponse:

    def __init__(self) -> None:
        self.API_BASE_URL = f"https://api.cloudflare.com/client/v4/accounts/{environ.get('CF_ACCOUNT_ID')}/ai/run/"
        self.headers = {"Authorization": f"Bearer {environ.get('CF_WORKER_AI_TOKEN')}"}




    def generate_response(self, query, mood_style, language_style):

        def run(model, inputs):
            input = { "messages": inputs }
            session = requests.Session()
            response = session.post(f"{self.API_BASE_URL}{model}", headers=self.headers, json=input)
            return response.json()
        
        inputs = [
            { "role": "system", "content": f"Your name is 'Moody' whose mood keep changing. Right now your mood is {mood_style} and response you will generate will be {language_style} and complete." },
            { "role": "user", "content": f"{query}"}
        ]
        output = run("@cf/meta/llama-2-7b-chat-fp16", inputs)

        return output