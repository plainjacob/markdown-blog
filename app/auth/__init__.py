from flask import Blueprint

# Create the blueprint
bp = Blueprint('auth', __name__)

from app.auth import routes