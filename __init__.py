from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__,static_folder='./templates/static')
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
app.static_folder = 'static'