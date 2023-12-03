from pymongo import MongoClient
from bson import ObjectId

class Chest:
    def __init__(self, rarity, XpAmount, numDiffCards, gold, timeToOpen):
        self.rarity = rarity
        self.XpAmount = XpAmount
        self.numDiffCards = numDiffCards
        self.gold = gold
        self.timeToOpen = timeToOpen

    def to_dict(self):
        return {
            "_id": ObjectId(),
            "rarity": self.rarity,
            "XpAmount": self.XpAmount,
            "numDiffCards": self.numDiffCards,
            "gold": self.gold,
            "timeToOpen": self.timeToOpen.isoformat() if self.timeToOpen else None
        }