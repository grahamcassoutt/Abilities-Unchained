from pymongo import MongoClient
from bson import ObjectId

class CardUsed:
    def __init__(self, characterId):
        self.characterId = characterId

class Game:
    def __init__(self, timestamp, playerAId, playerBId, winner, playerACardsUsedIds, playerBCardsUsedIds):
        self.timestamp = timestamp
        self.playerAId = playerAId
        self.playerBId = playerBId
        self.winner = winner
        self.playerACardsUsedIds = playerACardsUsedIds
        self.playerBCardsUsedIds = playerBCardsUsedIds

    def to_dict(self):
        return {
            "_id": ObjectId(),
            "timestamp": self.timestamp.isoformat() if self.timestamp else None,
            "playerAId": self.playerAId,
            "playerBId": self.playerBId,
            "winner": self.winner,
            "playerACardsUsedIds": [{"characterId": card.characterId} for card in self.playerACardsUsedIds],
            "playerBCardsUsedIds": [{"characterId": card.characterId} for card in self.playerBCardsUsedIds]
        }
