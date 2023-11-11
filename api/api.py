import logging
from flask import Flask
from pymongo import MongoClient
import constants
from endpoints.character.characterEndpoints import CharacterEndpoints
from endpoints.character.routes import setup_routes
# from endpoints.user import userBlueprint

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

# DB_URI = 'mongodb+srv://JMarch12:{}@abilities-unchained.5mrctok.mongodb.net/?retryWrites=true&w=majority'.format(constants.USER_PASSWORD)

mongo = MongoClient(constants.DB_URI)
db = mongo[constants.DATABASE_NAME]

# app.register_blueprint(CharacterEndpoints(db), url_prefix="/api/character")
# app.register_blueprint(userBlueprint, url_prefix="/api/user")

character_endpoints = CharacterEndpoints(db)
setup_routes(app, character_endpoints)

if __name__ == '__main__':
    app.run()