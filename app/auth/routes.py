from flask import render_template
from app.auth import auth_bp
from app.forms import RegisterForm

@auth_bp.route('/register')
def register():
  form = RegisterForm()

  return render_template('auth.html', form=form)