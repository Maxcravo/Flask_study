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

def getfile():
  root = tk.Tk()
  root.withdraw()
  file_path = filedialog.askopenfilename()
  return file_path

def text_summary():
  nest_asyncio.apply()
  llm = Groq(model="llama3-8b-8192")
  Settings.llm = llm
  Settings.embed_model = HuggingFaceEmbedding()
  file_path = getfile()
  # implementar essa funcão de uma forma que ele leia todos o arquivo pdf do diretório sem a necessidade de passar o nome dele
  documents = SimpleDirectoryReader(input_files=[file_path]).load_data()
  print(documents)