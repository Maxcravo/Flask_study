from flask import Blueprint

bp = Blueprint("camera", __name__)

from flask_src.camera import routes