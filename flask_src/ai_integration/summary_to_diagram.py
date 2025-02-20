from flask_src.models.model_util import get_summary
from llama_index.llms.groq import Groq
from llama_index.core.llms import ChatMessage, MessageRole
from llama_index.core.prompts import PromptTemplate
from pydantic import BaseModel
from dotenv import load_dotenv
import json
import os
load_dotenv()

class Diagram(BaseModel):
  """Descrição do prompt para o diagrama"""
  summary: str

def summary_to_diagram(diagram_title):
  llm = Groq(model="deepseek-r1-distill-qwen-32b", pydantic_program_mode="llm", api_key = os.environ.get("GROQ_API_KEY"))
  summary_db = get_summary(diagram_title)
  if isinstance(summary_db, tuple):
    summary_db = summary_db[0].get_data(as_text=True) # forma como recebemos e lemos nossa mensagem, a resposta vem como uma tupla, onde o primeiro elemento é a resposta
    print("Resposta do função:", summary_db)
  else:
    summary_db = str(summary_db)
  print("Resposta do DB:", summary_db)
  # prompt_template = PromptTemplate("translate the text to portuguese: {summary}")
  try:
    #TODO Ver como é possível fazer um diagrama a partir de um texto
    # response = llm.structured_predict(Diagram, prompt_template, summary = summary_db)
    # response = llm.complete(prompt=f"transform the given summary in a plantUML Activity Diagram syntax, the summary: {summary_db}, for example the plantUML syntax its like: @startumlstart :Hello world; :This is defined on several **lines**; end @enduml")
    plantuml_context = [
      ChatMessage(role= MessageRole.USER, 
                  content= f""" the syntax of the plantuml is: Simple action @startuml 
                  :Hello world; :This is defined on several **lines**; @enduml 
                  conditional: @startuml
                  start if (Graphviz installed?) then (yes) :process all\ndiagrams; else (no) :process only __sequence__ and __activity__ diagrams; endif stop @enduml 
                  Several tests (horizontal mode)
                  @startuml
                  start
                  if (condition A) then (yes)
                    :Text 1;
                  elseif (condition B) then (yes)
                    :Text 2;
                    stop
                  (no) elseif (condition C) then (yes)
                    :Text 3;
                  (no) elseif (condition D) then (yes)
                    :Text 4;
                  else (nothing)
                    :Text else;
                  endif
                  stop
                  @enduml
                  
                  Switch and case [switch, case, endswitch]
                  @startuml
                  start
                  switch (test?)
                  case ( condition A )
                    :Text 1;
                  case ( condition B ) 
                    :Text 2;
                  case ( condition C )
                    :Text 3;
                  case ( condition D )
                    :Text 4;
                  case ( condition E )
                    :Text 5;
                  endswitch
                  stop
                  @enduml
                  
                  Conditional with stop on an action [kill, detach]
                  
                  @startuml
                  if (condition?) then
                    :error;
                    stop
                  endif
                  #palegreen:action;
                  @enduml
                  """)]
    print(summary_db)
    # response = llm.achat_with_tools(chat_history=plantuml_context, user_msg= f"create a plantuml diagram that summary the given text, the text", verbose=True)
    response = llm.chat(messages=plantuml_context)
    print(response)
  except Exception as e:
    print(e)
  return response
  