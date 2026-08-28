from flask import Blueprint

posts_bp = Blueprint('main', __name__)

from app.posts import routes