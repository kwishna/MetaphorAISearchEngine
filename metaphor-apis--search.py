import os

import requests
import dotenv

dotenv.load_dotenv()

url = "https://api.metaphor.systems/search"

payload = {
    "query": "Here is an article about the state of search:",
    "numResults": 10,
    "includeDomains": ["example.com", "sample.net"],
    "excludeDomains": ["excludedomain.com", "excludeme.net"],
    "startCrawlDate": "2023-01-01",
    "endCrawlDate": "2023-12-31",
    "startPublishedDate": "2023-01-01",
    "endPublishedDate": "2023-12-31",
    "useAutoprompt": True,
    "type": "string"
}

headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "x-api-key": os.getenv("METAPHOR_API_KEY")
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)
