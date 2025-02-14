from extensions import db
from flask_src.models.model import *
from flask import jsonify
from sqlalchemy.exc import SQLAlchemyError
import inspect

# função para realizar o processo de insert no banco de dados.
def insert_summary(db_class, class_data):
  if not db_class or not class_data:
    return jsonify({"error: missing db_class or class_data"}), 500
  if inspect.isclass(db_class) != True:
    return jsonify({"error: the variable is not a class"}), 500
  try:
    insert = db_class(
      title = "new",
      summary = class_data
    )
    db.session.add(insert)
    db.session.commit()
  except SQLAlchemyError as e:
    db.session.rollback()
    return jsonify({"error": str(e)}), 500
  
def get_summary(summary_title):
  if not summary_title:
     return jsonify({"error: missing summary title"}), 500
  try:
    response = db.session.query(Ai_summary).filter_by(title = summary_title).first()
    # print(f"resposta do database: {response.summary}")
    if response is not None:
      return response.summary
  except SQLAlchemyError as e:
    db.session.rollback()
    return jsonify({"error": str(e)}), 500