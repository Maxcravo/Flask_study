from flask_src.ai_integration import bp
from flask_src.ai_integration.controller import text_summary
from flask_src.models.model import Ai_summary
from flask_src.models.model_util import insert_summary, get_summary
from sqlalchemy.exc import SQLAlchemyError
from extensions import db
from flask import jsonify

#! Tudo isso tem que ser feito no controlador a rota tem que só definir a rota e receber as funções do controlador

@bp.route("/ai")
def initialize_ai():
  try:
    response = text_summary()
    if not response:
      return jsonify({"error": "failed in summary generation"}), 500
     
  # Fazendo insert no database
    insert_summary(Ai_summary, response)

    return jsonify({
      "message": "summary created!"
    }), 200
  
  except Exception as e:
    db.session.rollback()
    return jsonify({"error": str(e)}), 500
  
@bp.route("/ai/get")
def initialize_file():
  try:
    response = get_summary()
    return response
  except Exception as e:
    return e
   
  # #! the right way
  # docs = db.session.query(Ai_summary).all()
  # for doc in docs:
  #     print(f"ID: {doc.id}")
  #     print(f"Title: {doc.title}")
  #     print(f"Summary: {doc.summary}")
  #     retorno = f"{str(doc.id)} + {doc.title} + {doc.summary}"
  # return jsonify({"return": str(retorno)}), 200