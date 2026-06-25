from flask import Flask
from pymongo import MongoClient
from .config import Config

client = None
db = None

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    global client, db
    client = MongoClient(app.config["MONGO_URI"])
    db = client[app.config["DB_NAME"]]
    
    from .routes import main
    app.register_blueprint(main)
    return app