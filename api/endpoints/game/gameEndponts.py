from flask import request, jsonify
from models.game import Game, CardUsed
from .gameModel import GameModel
import logging

class GameEndpoints:
    def __init__(self, db):
        self.collection = db['games']
        self.gameModel = GameModel(db)
    
    def get_game_by_id(self, gameId):
        game = self.gameModel.get_game_by_id(str(gameId))
        if game:
            return Game.from_dict(game).to_dict()
        else:
            return {"message": "game not found"}, 404

    def create_game(self):
        data = request.get_json()
        try:
            gameInstance = Game.from_dict(data)
            gameId = self.gameModel.create_game(gameInstance)
            return {"gameId": gameId}, 201
        except Exception as e:
            logging.error(f"Failed to create game: {str(e)}")
            return {"message": f"Failed to create game: {str(e)}"}, 500
    
    def delete_game(self, gameId):
        try:
            if self.gameModel.delete_game(gameId):
                return {"message": "game deleted successfully"}, 204
            else:
                return {"message": "game not found or delete failed"}, 404

        except Exception as e:
            return {"message": f"Failed to delete game: {str(e)}"}, 500
        