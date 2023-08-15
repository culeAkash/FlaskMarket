


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from market.db_config import get_db_config


app = Flask(__name__)

db_details = get_db_config()
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://{db_details.get('user')}:{db_details.get('password')}@{db_details.get('host')}:{db_details.get('port')}/{db_details.get('database')}"

db = SQLAlchemy(app)


from market import routes