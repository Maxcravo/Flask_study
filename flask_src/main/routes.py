# importamos a instancia do blueprint do nosso __init__.py
from flask_src.main import bp

@bp.route("/")
def index():
  return "The main blueprint of the aplication"