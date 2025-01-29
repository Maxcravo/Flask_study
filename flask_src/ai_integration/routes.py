from flask_src.ai_integration import bp
from flask_src.ai_integration.controller import text_summary, getfile
from flask_src.models.model import Ai_summary
from sqlalchemy.exc import SQLAlchemyError
from extensions import db
from flask import jsonify

@bp.route("/ai/")
def initialize_ai():
  try:
    response = text_summary()
    if not response:
      return jsonify({"error": "failed in summary generation"}), 500
     
  # Fazendo insert no database
    insert = Ai_summary(
      title="first Insert", summary = response)
    
    db.session.add(insert)
    db.session.commit()
    
    return jsonify({
      "message": "summary created!"
    }), 200
  
  except SQLAlchemyError as e:
    db.session.rollback()
    return jsonify({"error": str(e)}), 500
  
@bp.route("/ai/get")
def initialize_file():
  #! the ugly and bad way to recovery a data in sqlAlchemy
  # summary_all = Ai_summary.query.all()
  # for doc in summary_all:
  #   print (doc.summary)
  #! the right way
  docs = db.session.query(Ai_summary).filter_by(title="first Insert").all()
  for doc in docs:
      print(f"ID: {doc.id}")
      print(f"Title: {doc.title}")
      print(f"Summary: {doc.summary}")
  return None