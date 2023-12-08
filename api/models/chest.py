from pymongo import MongoClient
from bson import ObjectId

class Chest:
    def __init__(self, rarity, xpAmount, numDiffCards, gold, timeToOpen, _id=None):
        self._id = _id
        self.rarity = rarity
        self.xpAmount = xpAmount
        self.numDiffCards = numDiffCards
        self.gold = gold
        self.timeToOpen = timeToOpen

    def to_dict(self):
        chest_dict = {
            "_id": ObjectId(),
            "rarity": self.rarity,
            "xpAmount": self.xpAmount,
            "numDiffCards": self.numDiffCards,
            "gold": self.gold,
            "timeToOpen": self.timeToOpen
        }

        if self._id is not None:
            chest_dict["_id"] = str(self._id)

        return chest_dict
    
    @classmethod
    def from_dict(cls, chest_dict):
        rarity = chest_dict.get("rarity")
        xpAmount = chest_dict.get("xpAmount")
        numDiffCards = chest_dict.get("numDiffCards")
        gold = chest_dict.get("gold")
        timeToOpen = chest_dict.get("timeToOpen")

        _id = str(chest_dict.get("_id", ObjectId()))

        return cls(rarity, xpAmount, numDiffCards, gold, timeToOpen, _id)
    
    def to_dict_for_update(self):
        chest_dict = {
            key: value
            for key, value in self.to_dict().items()
            if key != '_id' and value is not None
        }
        return chest_dict
