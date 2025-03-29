import nest_asyncio
from llama_index.llms.groq import Groq
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core import SimpleDirectoryReader
from llama_index.core import SummaryIndex 
from llama_index.core.memory import ChatMemoryBuffer
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import Settings, VectorStoreIndex
from dotenv import load_dotenv
import re
import os
load_dotenv()

def initialize_groq():
  """ Initialize the Groq LLM and set it as the default LLM in the Settings."""
  try:
    llm = Groq(model="deepseek-r1-distill-qwen-32b", api_key= os.getenv("GROQ_API_KEY"))
    Settings.llm = llm
    Settings.embed_model = HuggingFaceEmbedding()
    return llm
  except Exception as e:
    print(f"error {e}")

def summary(file_path):
  print(f"file location: {file_path}, api key: {os.getenv('GROQ_API_KEY')}")
  nest_asyncio.apply()
  try:
    llm = initialize_groq()
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
    # response = str(response.response).split("<think/>")[1]
    response = response.response
    diagram_response = summary_diagram(response)
    response_return = str(response + "\n \n" + diagram_response)
  except Exception as e:
    print(f"\n \n problem with the return of the Groq API: {e} \n \n")
    # Inicio o summary que vai criar um summario com base no texto dado pelo usuario
  return response_return

def summary_diagram(summary_response):
  # llm = initialize_groq()
  dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
  example_path = os.path.join(dir, "data", "example.txt")
  context = SimpleDirectoryReader(input_files=[example_path]).load_data()
  index = VectorStoreIndex.from_documents(context)
  memory = ChatMemoryBuffer.from_defaults(token_limit=2048)
  llm_chat = index.as_chat_engine(
    chat_mode="context",
    memory=memory,
  )
  try:
    response = llm_chat.chat(f"create a diagram that summary the text given by the user, using the syntax alread given by the user. the text is {summary_response}")
    response = response.response  
  except Exception as e:
    print(f"problem with the creation of the diagram: {e}")\
  # usamos essa parte para extrair apenas a parte necessária da resposta.
  return response