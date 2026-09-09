from flask import Flask
from app.config import config
from app.extensions import db, migrate, login_manager, pages


def create_app(config_name='development'):
  # Create the Flask application instance
  app = Flask(__name__)

  # Load configuration from config class
  app.config.from_object(config[config_name])

  # Initialize extensions with this app instance
  db.init_app(app)
  migrate.init_app(app, db)
  login_manager.init_app(app) 
  pages.init_app(app)

  # from app.models.user import User
  # @login_manager.user_loader
  # def load_user(user_id):
  #     return User.query.get(int(user_id))

  # Register blueprints
  from app.main import bp as main_bp
  app.register_blueprint(main_bp)

  from app.auth import bp as auth_bp
  app.register_blueprint(auth_bp)

  from app.posts import bp as posts_bp
  app.register_blueprint(posts_bp)

  return app


from app import models