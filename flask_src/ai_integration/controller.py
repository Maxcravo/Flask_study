import os
import tkinter as tk
from tkinter import filedialog
from llama_index.core import SimpleDirectoryReader
from llama_index.core import SummaryIndex 
from llama_index.llms.groq import Groq
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core import Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
import nest_asyncio
os.environ["GROQ_API_KEY"]

#!Uma outra forma de tilizar o tk do python de modo que não pare a execucão principal( main thread) é usar o asyncio para forcar o mesmo e rodar em um
# thread diferente, lembrando que a própria biblioteca do tk não suporta async
# criamos a funcão que vai forcar o Tk a rodar de forma assincrona, criamos um event loop e rodamos nossa funcão sync_getfile nele
# async def getfile_async():
#   # cria um weaper
#   loop = asyncio.get_running_loop()
#   return await loop.run_in_executor(None, sync_getfile )
# # A funcão get)file
# def sync_getfile():
#   root = tk.Tk()
#   root.withdraw()
#   file_path = filedialog.askopenfile()
#   root.destroy()
#   return file_path
  
# async def get_async():
#   try:
#     file = await getfile()
#   except Exception as e:
#     print(e)
#     return None

def getfile():
  root = tk.Tk()
  root.withdraw()
  file_path = filedialog.askopenfilename()
  root.destroy()
  return file_path

def text_summary():
  nest_asyncio.apply()
  # Connecting to groq and set the model, dowloading embedding
  try:
    llm = Groq(model="llama3-8b-8192")
    Settings.llm = llm
    Settings.embed_model = HuggingFaceEmbedding()
  except Exception as e : #TODO aqui tem que retornar um erro
    return print(f"error in get connect to Groq or dowload hugging face Embed: {e}")
  # getting the file from user
  file_path = getfile()
  documents = SimpleDirectoryReader(input_files=[file_path]).load_data()
  
  #spliting the given file in nodes to summarize
  splitter = SentenceSplitter(chunk_size=2024)
  nodes = splitter.get_nodes_from_documents(documents)
  summary_query = SummaryIndex(nodes).as_query_engine(
    response_mode = "tree_summarize",
    use_async= True
  )
  try:
    response = summary_query.query("summarize in detail the given document but not surpass 10k tokens")
  except Exception as e:
    print(f"problem with the return of the Groq API: {e}")
  return response