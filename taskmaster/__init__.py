from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

SECRET_KEY = os.environ.get("SECRET_KEY")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///main.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SECRET_KEY"] = SECRET_KEY
db = SQLAlchemy(app)

from taskmaster import views, models