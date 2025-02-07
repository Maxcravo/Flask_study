from flask_src.db_controler import bp
from flask_src.db_controler.controller import set_db

@bp.route("/db")
def db_init():
  set_db()
  return "db sync"