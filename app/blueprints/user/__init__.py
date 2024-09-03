from flask import Blueprint

user = Blueprint("user", __name__)

from app.blueprints.user import model
from app.blueprints.user import routes
