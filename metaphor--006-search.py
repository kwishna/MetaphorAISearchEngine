import os

import dotenv
from metaphor_python import Metaphor
from metaphor_python.metaphor import SearchRequest, GetContentsResponse

dotenv.load_dotenv()

metaphor = Metaphor(os.getenv("METAPHOR_API_KEY"))

search_request = SearchRequest(
    query="Here is news about the American supreme court:",
    include_domains=["nytimes.com"],
    start_published_date="2023-06-25"
)

search_response = metaphor.search(
    "Here is news about the American supreme court:",
    include_domains=["nytimes.com"],
    start_published_date="2023-06-25",
)

contents_response: GetContentsResponse = search_response.get_contents()

# Print content for each result
for content in contents_response.contents:
    print(f"Title: {content.title}")
    print(f"URL: {content.url}")
    print(f"Content: S{content.extract}")
