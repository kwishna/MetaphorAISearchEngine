import os
from metaphor_python import Metaphor
import dotenv

dotenv.load_dotenv()

metaphor = Metaphor(os.getenv("METAPHOR_API_KEY"))

response = metaphor.search(
  "Top 10 Indian scientists in 2023",
  num_results=2,
  use_autoprompt=True,
)

for result in response.results:
    print("------------------------------------------------------------------------------------------------------------------------")
    print("Title: ", result.title)
    print("Url: ", result.url)
    print("Score: ", result.score)
    print("published_date: ", result.published_date)
    print("Author: ", result.author)
    print("Extract: ", result.extract)