from flask import render_template
from app.main import bp 
from app.extensions import pages
from app.config import Config

# INDEX
@bp.route('/')
def index():
  posts = [p for p in pages if p.path.startswith(Config.POST_DIR)]
  latest = sorted(posts, reverse=True,
                  key=lambda p: p.meta['date'])[0]
  return render_template('index.html', title='Home', latest=latest)

# PROFILE
@bp.route('/<user>')
def profile(user):
  return render_template('profile.html', title='Profile')