from flask import render_template, flash, redirect, url_for, request
from app.main import bp 
from app.extensions import db, pages
from app.config import Config
from flask_login import login_required, current_user
from app.models.user import User
from app.forms import EditProfileForm
import sqlalchemy as sa

# INDEX
@bp.route('/')
def index():
  posts = [p for p in pages if p.path.startswith(Config.POST_DIR)]
  latest = sorted(posts, reverse=True,
                  key=lambda p: p.meta['date'])[0]
  return render_template('index.html', title='Home', latest=latest)

# ABOUT
@bp.route('/about')
def about():
  return render_template('about.html', title='About')


# PROFILE
@bp.route('/<username>')
@login_required
def profile(username):
  user = db.first_or_404(sa.select(User).where(User.username == username))
  return render_template('profile.html', title='Profile', user=user)

# EDIT PROFILE
@bp.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
  form = EditProfileForm()
  if form.validate_on_submit():
    current_user.username = form.username.data
    db.session.commit()
    flash('Your changes have been saved.')
    return redirect(url_for('main.edit_profile'))
  elif request.method == 'GET':
    form.username.data = current_user.username
  return render_template('edit_profile.html', title='Edit Profile', form=form)