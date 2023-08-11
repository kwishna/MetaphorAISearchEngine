import os

import dotenv
from metaphor_python import Metaphor, SearchResponse
dotenv.load_dotenv()

metaphor = Metaphor(os.getenv("METAPHOR_API_KEY"))

response: SearchResponse = metaphor.find_similar(
    "https://phys.org/news/2023-06-einstein-euler-expansion-universe-dark.html",
    num_results=2,
)

for result in response.results:
    print("------------------------------------------------------------------------------------------------------------------------")
    print("Title: ", result.title)
    print("Url: ", result.url)
    print("Score: ", result.score)
    print("published_date: ", result.published_date)
    print("Author: ", result.author)
    print("Extract: ", result.extract)
