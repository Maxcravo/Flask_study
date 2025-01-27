from flask import Blueprint

bp = Blueprint("ai_integration", __name__)

from flask_src.ai_integration import routes
