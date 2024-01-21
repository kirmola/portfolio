import requests

def generate_response(query, mood_style, language_style):
    API_BASE_URL = "https://moody.amanrawat.workers.dev/"
    inputs = {
        "query":query,
        "mood_style":mood_style,
        "language_style":language_style
    }
    with requests.get(API_BASE_URL, params=inputs, stream=True) as response:
        for each in response:
            yield each
        