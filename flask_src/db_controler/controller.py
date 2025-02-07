from extensions import db
from sqlalchemy.orm import Session
from flask_src.models.model import Ai_summary

# Lembrar que primeiro é importante saber que precisamos instanciar nossa classe e não
# podemos diretamente ir e adicionar e commitar a classe.

def set_db():
  try:
    db.create_all() # Usa Create_all antes de definir a instancia da classe
    ai_summary_instance = Ai_summary(title="test", summary= "test1")
    db.session.add(ai_summary_instance)
  except Exception as e:
    db.session.rollback()
    print(f"error sql Alchemy: {e}")
    raise
  else:
    db.session.commit()
    print("class created!")