import os
from typing import List

from metaphor_python import Metaphor, GetContentsResponse, DocumentContent
import dotenv

dotenv.load_dotenv()

metaphor = Metaphor(os.getenv("METAPHOR_API_KEY"))

ids=["fRZd_DYpWEAxrLhfv2ctsg"]
contents_result: GetContentsResponse = metaphor.get_contents(ids)
results: List[DocumentContent] = contents_result.contents

for result in results:
    print("------------------------------------------------------------------------------------------------------------------------")
    print(f"Id: {result.id}")
    print(f"Title: {result.title}")
    print(f"URL: {result.url}")
    print(f"Content: S{result.extract}")

