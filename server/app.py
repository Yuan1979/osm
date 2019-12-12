import os
from flask import Flask
from domain import db
from api import create_api
from config import Config
from flask_cors import CORS 

def create_app():
    flask_app = Flask(__name__)
    flask_app.config.from_object(Config)
    db.init_app(flask_app)
    create_api(flask_app)
    return flask_app

app = create_app()
CORS(app)