import os

import dotenv
import openai
from metaphor_python import Metaphor

dotenv.load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

metaphor = Metaphor(os.getenv("METAPHOR_API_KEY"))

## Step - 1
USER_QUESTION = "What's the recent news on physics today?"

SYSTEM_MESSAGE = "You are a helpful assistant that generates search queiries based on user questions. Only generate one search query."

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": SYSTEM_MESSAGE},
        {"role": "user", "content": USER_QUESTION},
    ],
)

query = completion.choices[0].message.content

print(f'Query: {query}')  # Recent developments in physics news

## Step - 2
search_response = metaphor.search(
    query + "are :",
    use_autoprompt=True,
    start_published_date="2023-06-01",
    num_results=2
)

for result in search_response.results:
    print("--------------------------------------------------------------------------------")
    print("Result url: ", result.url)
    print("Result title: ", result.title)
    print("Result extract: ", result.extract)

## Step - 3

# Summarize content of first result.

SYSTEM_MESSAGE = "You are a helpful assistant that summarizes the content of a webpage. Summarize the users input."

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": SYSTEM_MESSAGE},
        {"role": "user", "content": search_response.get_contents().contents[0].extract},
        # Korean team claims to have created the first room-temperature, ambient-pressure superconductor
        # `search_response.get_contents().contents[0].extract` should be a string not None
    ],
)

summary = completion.choices[0].message.content
print(f"Summary for {search_response.results[0].title}: {summary}")
