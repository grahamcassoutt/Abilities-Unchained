from flask import request, jsonify
from models.game import Game, CardUsed
from .gameModel import GameModel
import logging

class GameEndpoints:
    def __init__(self, db):
        self.collection = db['games']
        self.gameModel = GameModel(db)
    
    def get_game_by_id(self, gameId):
        game = self.gameModel.get_game_by_id(gameId)
        if game:
            return game.from_dict(game).to_dict()
        else:
            return {"message": "game not found"}, 404

    def create_game(self, data):
        if not data:
            return {"message": "No data provided in the request"}, 400

        try:
            playerAIds = data.get("playerACardsUsedIds", [])
            playerBIds = data.get("playerBCardsUsedIds", [])

            playerAIdsList = [
                CardUsed(
                    characterId=ids.get("characterId")
                ) for ids in playerAIds
            ]

            playerBIdsList = [
                CardUsed(
                    characterId=ids.get("characterId")
                ) for ids in playerBIds
            ]

            game = Game(
                timestamp=data.get("timestamp"),
                playerAId=data.get("playerAId"),
                playerBId=data.get("playerBId"),
                winner=data.get("winner"),
                playerACardsUsedIds=playerAIdsList,
                playerBCardsUsedIds=playerBIdsList
            )

            gameId = self.gameModel.create_game(game)
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
        