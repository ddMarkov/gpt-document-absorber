from dotenv import load_dotenv
from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader

load_dotenv()  # take environment variables from .env.

documents = SimpleDirectoryReader('data').load_data()
index = GPTSimpleVectorIndex.from_documents(documents)

response = index.query("What did the author do growing up?")
print(response)

