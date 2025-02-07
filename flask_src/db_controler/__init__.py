from flask import Blueprint

bp = Blueprint("db_controler", __name__)

from flask_src.db_controler import routes