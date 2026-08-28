from flask_login import UserMixin
from app.extensions import db, login_manager

class User(UserMixin, db.Model):
  __tablename__ = "user"

  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(80), unique=True, nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  password = db.Column(db.String(300), nullable=False, unique=True)
  created_at = db.Column(db.DateTime, default=db.func.now())

  def __repr__(self):
    return '<User %r> ' % self.username

@login_manager.user_loader
def load_user(user_id):
  """Load user by ID for Flask-Login."""
  return User.query.get(int(user_id))