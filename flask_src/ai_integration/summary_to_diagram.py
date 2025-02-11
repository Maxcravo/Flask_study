from flask_src.models.model_util import get_summary
from llama_index.llms.groq import Groq
from llama_index.core.prompts import PromptTemplate
from pydantic import BaseModel
from dotenv import load_dotenv
import os
load_dotenv()

class Diagram(BaseModel):
  """Descrição do prompt para o diagrama"""
  summary: str

def summary_to_diagram(diagram_title):
  llm = Groq(model="llama3-70b-8192", pydantic_program_mode="llm", api_key = os.environ.get("GROQ_API_KEY"))
  summary_db = get_summary(diagram_title)
  if isinstance(summary_db, dict):
    summary_db = summary_db.get("summary", "")
  else:
    summary_db = str(summary_db)
  print("Resposta do DB:", summary_db)
  prompt_template = PromptTemplate("Convert the following process into Mermaid flowchart syntax: {summary}")
  try:
    #TODO Ver como é possível fazer um diagrama a partir de um texto
    response = llm.structured_predict(Diagram, prompt_template, summary = "I am max and i Have a dog, my dog is only mine.")
  except Exception as e:
    print(e)
  print(f"resposta:", response)
  