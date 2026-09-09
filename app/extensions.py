from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_flatpages import FlatPages

# Create extension instances without app
# These will be initialized in create_app()
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
pages = FlatPages()

# Configure login manager
login_manager.login_view = 'auth.login'
login_manager.login_message = 'Please log in to access this page.'