import os
import requests
import dotenv

dotenv.load_dotenv()

url = f"https://api.metaphor.systems/contents?ids=fRZd_DYpWEAxrLhfv2ctsg&ids=fRZd_DYpWEAxrLhfv2ctsg"

headers = {
    "accept": "application/json",
    "x-api-key": os.getenv("METAPHOR_API_KEY")
}

response = requests.get(url, headers=headers)

print(response.text)
