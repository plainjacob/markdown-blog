from flask import render_template
from app.main import bp 

# INDEX
@bp.route('/')
def index():
  return render_template('index.html', title='Home')

# PROFILE
@bp.route('/<user>')
def profile(user):
  return render_template('profile.html', title='Profile')