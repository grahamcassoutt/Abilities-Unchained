from pymongo import MongoClient
from bson import ObjectId

class CardUsed:
    def __init__(self, characterId):
        self.characterId = characterId

    @classmethod
    def from_dict(cls, card_dict):
        return cls(characterId=card_dict['characterId'])

class Game:
    def __init__(self, timestamp, playerAId, playerBId, winner, playerACardsUsedIds, playerBCardsUsedIds, _id=None):
        self._id = _id
        self.timestamp = timestamp
        self.playerAId = playerAId
        self.playerBId = playerBId
        self.winner = winner
        self.playerACardsUsedIds = playerACardsUsedIds
        self.playerBCardsUsedIds = playerBCardsUsedIds

    def to_dict(self):
        game_dict = {
            "_id": ObjectId(),
            "timestamp": self.timestamp.isoformat() if self.timestamp else None,
            "playerAId": self.playerAId,
            "playerBId": self.playerBId,
            "winner": self.winner,
            "playerACardsUsedIds": [{"characterId": card.characterId} for card in self.playerACardsUsedIds],
            "playerBCardsUsedIds": [{"characterId": card.characterId} for card in self.playerBCardsUsedIds]
        }

        if self._id is not None:
            game_dict["_id"] = str(self._id)

        return game_dict
    
    @classmethod
    def from_dict(cls, game_dict):
        timestamp = game_dict.get('timestamp')
        playerAId = game_dict['playerAId']
        playerBId = game_dict['playerBId']
        winner = game_dict['winner']
        playerACardsUsedIds = [CardUsed.from_dict(card_dict) for card_dict in game_dict['playerACardsUsedIds']]
        playerBCardsUsedIds = [CardUsed.from_dict(card_dict) for card_dict in game_dict['playerBCardsUsedIds']]

        _id = str(game_dict.get("_id", ObjectId()))

        return cls(timestamp, playerAId, playerBId, winner, playerACardsUsedIds, playerBCardsUsedIds, _id)
