from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from market.db_config import get_db_config
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

db_details = get_db_config()
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://{db_details.get('user')}:{db_details.get('password')}@{db_details.get('host')}:{db_details.get('port')}/{db_details.get('database')}"

app.config['SECRET_KEY'] = '84effd341115cc673704ffc9'

db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category = 'info'

from market import routes