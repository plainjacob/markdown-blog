import sqlalchemy as sa
from flask import flash, render_template, redirect, url_for
from flask_login import current_user, login_user, logout_user
from app.auth import bp
from app.forms import RegisterForm, LoginForm
from app.models.user import User
from app.extensions import db

@bp.route('/register', methods=['GET', 'POST'])
def register():
  # Check if current user is authenticated before logging in
  if current_user.is_authenticated:
    return redirect(url_for('main.index'))
  
  form = RegisterForm()

  if form.validate_on_submit():
    # Create new user object
    user = User(username=form.username.data, email=form.password.data)
    user.set_password(form.password.data)

    # Add user to the database
    db.session.add(user)
    db.session.commit()

    flash('Congratulations, you are now a registered user!')

    return redirect(url_for('auth.login'))
  return render_template('register.html', title="Register", form=form)


@bp.route('/login', methods=['GET', 'POST'])
def login():
  # Check if current user is authenticated before logging in
  if current_user.is_authenticated:
    return redirect(url_for('main.index'))
  
  form = LoginForm()
  if form.validate_on_submit():
    user = db.session.scalar(
      sa.select(User).where(User.username == form.username.data))

    # Validate user object
    if user is None:
      flash(f'User with the username {form.username.data} does not exist.')
      return redirect(url_for('auth.login'))

    # Check password
    elif not user.check_password(form.password.data):
      flash(f'Invalid password for the user {form.username.data}.')
      return redirect(url_for('auth.login'))

    login_user(user, remember=form.remember_me.data)
    flash('Succesfully logged in!')
    return redirect(url_for('main.index'))
  return render_template('login.html', title='Login', form=form)


@bp.route('/logout')
def logout():
  logout_user()
  return redirect(url_for('main.index'))