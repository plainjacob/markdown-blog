import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
  """Base configuration with settings common to all environments."""
  SECRET_KEY = os.environ.get('SECRET_KEY') or 'my_secret_key'
  FLATPAGES_EXTENSION = '.md'
  FLATPAGES_ROOT = 'content'
  POST_DIR = 'posts'

class DevelopmentConfig(Config):
  """Development configuration."""
  DEBUG = True
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')\
    or 'sqlite:///' + os.path.join(basedir, 'app.db')
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  FLATPAGES_AUTO_RELOAD = DEBUG

config = {
  'development': DevelopmentConfig
}