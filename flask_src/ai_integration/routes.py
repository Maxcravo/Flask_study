from flask_src.ai_integration import bp
from flask_src.ai_integration.controller import text_summary, summary
from flask_src.ai_integration.summary_to_diagram import summary_to_diagram
from flask_src.models.model import Ai_summary
from flask_src.models.model_util import insert_summary, get_summary
from sqlalchemy.exc import SQLAlchemyError
from extensions import db
from flask import jsonify, request
import json
import nest_asyncio

#! Tudo isso tem que ser feito no controlador a rota tem que só definir a rota e receber as funções do controlador

# tenho que ajeitar essa rota para receber os dados do servidor do next
@bp.route("/ai/data/", methods=["POST"])
async def get_data():
  if request.method == "POST":
    data = request.get_json()
    summary_data = await summary(data)
    if not summary_data:
      return jsonify({"error": "failed in summary generation"}), 500
    return str(summary_data)
  # return jsonify({"message": "GET request received"})
    

@bp.route("/ai", methods=["POST"])
def initialize_ai():
  if request.method == "POST":
    data = request.get_json()
    try:
      response = text_summary(data)
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
    response = get_summary(summary_title="first Insert")
  except Exception as e:
    return e
  return str(response)

@bp.route("/ai/diagram")
def initialize_diagram():
  response = str(summary_to_diagram(diagram_title="first Insert"))
  return response