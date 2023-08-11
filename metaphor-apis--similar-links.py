import requests

url = "https://api.metaphor.systems/findSimilar"

payload = {
    "url": "https://slatestarcodex.com/2014/07/30/meditations-on-moloch/",
    "numResults": 10,
    "includeDomains": ["example.com", "sample.net"],
    "excludeDomains": ["excludedomain.com", "excludeme.net"],
    "startCrawlDate": "2023-01-01",
    "endCrawlDate": "2023-12-31",
    "startPublishedDate": "2023-01-01",
    "endPublishedDate": "2023-12-31"
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "x-api-key": "ffff"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)