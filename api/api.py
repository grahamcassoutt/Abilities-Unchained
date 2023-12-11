import logging
from flask import Flask
from flask_cors import CORS
from pymongo import MongoClient
import constants
from endpoints.character.characterEndpoints import CharacterEndpoints
from endpoints.character.routes import setup_routes as CharacterRoutes
from endpoints.ability.abilityEndpoints import AbilityEndpoints
from endpoints.ability.routes import setup_routes as AbilityRoutes
from endpoints.chest.chestEndpoints import ChestEndpoints
from endpoints.chest.routes import setup_routes as ChestRoutes
from endpoints.relationship.relationshipEndpoints import RelationshipEndpoints
from endpoints.relationship.routes import setup_routes as RelationshipRoutes
from endpoints.game.gameEndponts import GameEndpoints
from endpoints.game.routes import setup_routes as GameRoutes
from endpoints.user.userEndpoints import UserEndpoints
from endpoints.user.routes import setup_routes as UserRoutes


app = Flask(__name__)
CORS(app)

# DB_URI = 'mongodb+srv://JMarch12:{}@abilities-unchained.5mrctok.mongodb.net/?retryWrites=true&w=majority'.format(constants.USER_PASSWORD)

mongo = MongoClient(constants.DB_URI)
db = mongo[constants.DATABASE_NAME]

logging.debug(db)

character_endpoints = CharacterEndpoints(db)
CharacterRoutes(app, character_endpoints)

ability_endpoints = AbilityEndpoints(db)
AbilityRoutes(app, ability_endpoints)

chest_endpoints = ChestEndpoints(db)
ChestRoutes(app, chest_endpoints)

relationship_endpoints = RelationshipEndpoints(db)
RelationshipRoutes(app, relationship_endpoints)

game_endpoints = GameEndpoints(db)
GameRoutes(app, game_endpoints)

user_endpoints = UserEndpoints(db)
UserRoutes(app, user_endpoints)

if __name__ == '__main__':
    app.run(port=7050, debug=True)