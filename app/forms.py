from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
import sqlalchemy as sa
from app.extensions import db
from app.models.user import User


class RegisterForm(FlaskForm):
  username = StringField('Username', validators=[DataRequired()])
  email = StringField('Email', validators=[DataRequired(), Email()])
  password = PasswordField('Password', validators=[DataRequired()])
  password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
  submit = SubmitField('Register')

  def validate_username(self, username):
    user = db.session.scalar(sa.select(User).where(
      User.username == username.data
    ))
    if user is not None:
      raise ValidationError('Username is already registered.')

  def validate_email(self, email):
    user = db.session.scalar(sa.select(User).where(
      User.email == email.data
    ))
    if user is not None:
      raise ValidationError('Email address is already registered.')

class LoginForm(FlaskForm):
  username = StringField('Username', validators=[DataRequired()])
  password = PasswordField('Password', validators=[DataRequired()])
  remember_me = BooleanField('Remember Me')
  submit = SubmitField('Sign In')