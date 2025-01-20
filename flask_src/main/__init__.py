from flask import Blueprint

bp = Blueprint('main', __name__)

from flask_src.main import routes
