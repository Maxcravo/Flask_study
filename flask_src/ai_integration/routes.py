from flask_src.ai_integration import bp
from flask_src.ai_integration.controller import text_summary, getfile

@bp.route("/ai/")
def initialize_ai():
  text_summary()
  return "getting ai summary"

# @bp.route("/getfile/")
# def initialize_file():
#   getfile()
#   return "return file path"