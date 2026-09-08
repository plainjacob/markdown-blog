from flask import render_template
from flask_login import login_required
from app.posts import bp 
from app.extensions import pages
from app.config import Config

@bp.route('/')
def index():
  return render_template('index.html', title='Index')

@bp.route('/posts')
@login_required
def posts():
  # Get posts 
  posts = [p for p in pages if p.path.startswith(Config.POST_DIR)]
  posts.sort(key=lambda item:item['date'], reverse=False)
  return render_template('posts.html', posts=posts)

@bp.route('/posts/<name>/')
def post(name):
  path = '{}/{}'.format(Config.POST_DIR, name)
  print(path)
  post = pages.get_or_404(path)
  return render_template('post.html', post=post)