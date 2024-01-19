import aiohttp
from os import environ

class GenerateResponse:

    def __init__(self) -> None:
        self.API_BASE_URL = f"https://api.cloudflare.com/client/v4/accounts/{environ.get('CF_ACCOUNT_ID')}/ai/run/"
        self.headers = {"Authorization": f"Bearer {environ.get('CF_WORKER_AI_TOKEN')}"}

    async def generate_response(self, query, mood_style, language_style):

        async def run(model, inputs):
            input_data = {"messages": inputs}
            async with aiohttp.ClientSession() as session:
                async with session.post(f"{self.API_BASE_URL}{model}", headers=self.headers, json=input_data) as response:
                    return await response.json()

        inputs = [
            {"role": "system", "content": f"Your name is 'Moody' whose mood keeps changing. Right now your mood is {mood_style} and the response you will generate will be {language_style} and complete."},
            {"role": "user", "content": f"{query}"}
        ]
        output = await run("@cf/meta/llama-2-7b-chat-fp16", inputs)

        return output
