from flask_src.ai_integration import bp
from flask_src.ai_integration.controller import text_summary, getfile

@bp.route("/ai/")
def initialize_ai():
  response = text_summary()
  return str(response)

# @bp.route("/getfile/")
# def initialize_file():
#   getfile()
#   return "return file path"