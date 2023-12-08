import logging
import pymongo
from bson.objectid import ObjectId

class GameModel:
    def __init__(self, db):
        self.collection = db['games']

    def create_game(self, game):
        game_document = game.to_dict()
        logging.debug(game_document)
        result = self.collection.insert_one(game_document)
        return str(result.inserted_id)

    def get_game_by_id(self, gameId):
        game = self.collection.find_one({"_id": ObjectId(gameId)})
        return game

    def delete_game(self, gameId):
        result = self.collection.delete_one({"_id": ObjectId(gameId)})
        return result.deleted_count > 0
