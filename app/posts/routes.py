from flask import redirect, render_template, url_for
from app.posts import posts_bp
from app.extensions import pages
from app.config import Config

@posts_bp.route('/')
def index():
  return redirect(url_for('main.posts'))

@posts_bp.route('/posts')
def posts():
  posts = [p for p in pages if p.path.startswith(Config.POST_DIR)]
  posts.sort(key=lambda item:item['date'], reverse=False)
  return render_template('posts.html', posts=posts)

@posts_bp.route('/posts/<name>/')
def post(name):
  path = '{}/{}'.format(Config.POST_DIR, name)
  print(path)
  post = pages.get_or_404(path)
  return render_template('post.html', post=post)