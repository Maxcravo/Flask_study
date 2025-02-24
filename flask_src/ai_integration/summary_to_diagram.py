from flask_src.models.model_util import get_summary
from llama_index.llms.groq import Groq
from llama_index.core.memory import ChatMemoryBuffer
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, output_parsers
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import Settings
from pydantic import BaseModel
from dotenv import load_dotenv
import json
import os
load_dotenv()

def summary_to_diagram(diagram_title):
  llm = Groq(model="deepseek-r1-distill-qwen-32b", api_key = os.environ.get("GROQ_API_KEY"))
  Settings.llm = llm
  Settings.embed_model = HuggingFaceEmbedding()
  summary_db = get_summary(diagram_title)
  if isinstance(summary_db, tuple):
    summary_db = summary_db[0].get_data(as_text=True) # forma como recebemos e lemos nossa mensagem, a resposta vem como uma tupla, onde o primeiro elemento é a resposta
    # print("Resposta do função:", summary_db)
  else:
    summary_db = str(summary_db)
  # print("Resposta do DB:", summary_db)
  try:
    #TODO Ver como é possível fazer um diagrama a partir de um texto
    #TODO essa parte de ler o arquivo deveria poder ser realizada apenas 1 vez
    path = "flask_src/data/uml_context.txt"
    uml_context = SimpleDirectoryReader(input_files=[path]).load_data()
    # print(f"leitura do txt: {uml_context}" )
    index = VectorStoreIndex.from_documents(uml_context)
    memory_string =  ChatMemoryBuffer.from_defaults(token_limit=1200)

    llm_chat = index.as_chat_engine(
      chat_mode="context",
      memory = memory_string,
      system_prompt= ("create a diagram that summary the text given by the user, using the activity diagram syntax already given. provide only the final answer without additional thoughts"),
    )
    response = llm_chat.chat( message=f"give me a diagram about: {summary_db}")
    response = str(response).split("```")[1]
    file_path = os.path.join("flask_src/data/saved_summary", f"{diagram_title}.txt" )
    with open(file_path,"x") as file_txt:
      file_txt.write(f"summary: \n \n {summary_db} \n \n  diagram: {response}")
    print(f"resposta depois do split: {response}")
  except Exception as e:
    print(e)
  return response
  