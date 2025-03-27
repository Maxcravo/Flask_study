import nest_asyncio
from llama_index.llms.groq import Groq
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core import SimpleDirectoryReader
from llama_index.core import SummaryIndex 
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import Settings
from dotenv import load_dotenv
import os
load_dotenv()

def summary(file_path):
  print(f"file location: {file_path}, api key: {os.getenv('GROQ_API_KEY')}")
  nest_asyncio.apply()
  try:
    llm = Groq(model="llama3-8b-8192", api_key= os.getenv("GROQ_API_KEY"))
    Settings.llm = llm
    Settings.embed_model = HuggingFaceEmbedding()
  except Exception as e:
    return print(f"error in connect to grog or dowload face Embed:{e}")
  response_list = []
  documents = SimpleDirectoryReader(input_files=[file_path]).load_data()
  print(f"loaded docs {documents}")
  splitter = SentenceSplitter(chunk_size=2024)
  nodes = splitter.get_nodes_from_documents(documents)
  summary_query = SummaryIndex(nodes).as_query_engine(
    response_mode = "tree_summarize",
    use_async= True
    )
  try:
    response = summary_query.query("summarize in detail the given document but not surpass 10k tokens")
    response_list.append(response)
  except Exception as e:
    print(f"problem with the return of the Groq API: {e}")
  return response.response