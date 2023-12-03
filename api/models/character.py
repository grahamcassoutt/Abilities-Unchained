import pymongo
from bson.objectid import ObjectId

class CharacterStatistics:
    def __init__(self, level, health, attack, xpToUpgrade, goldToUpgrade):
        self.level = level
        self.health = health
        self.attack = attack
        self.xpToUpgrade = xpToUpgrade
        self.goldToUpgrade = goldToUpgrade

class Character:
    def __init__(self, name, description, backOfCardDescription, photoUrl, soundEffect, unlockedAt, abilityId, characterStatistics, _id = None):
        self._id = _id
        self.name = name
        self.description = description
        self.backOfCardDescription = backOfCardDescription
        self.photoUrl = photoUrl
        self.soundEffect = soundEffect
        self.unlockedAt = unlockedAt
        self.abilityId = abilityId
        self.characterStatistics = characterStatistics

    def to_dict(self):
        character_dict = {
            "name": self.name,
            "description": self.description,
            "backOfCardDescription": self.backOfCardDescription,
            "photoUrl": self.photoUrl,
            "soundEffect": self.soundEffect,
            "unlockedAt": self.unlockedAt,
            "abilityId": self.abilityId if self.abilityId else None,
            "characterStatistics": [
                {
                    "level": stat.level,
                    "health": stat.health,
                    "attack": stat.attack,
                    "xpToUpgrade": stat.xpToUpgrade,
                    "goldToUpgrade": stat.goldToUpgrade
                }
                for stat in self.characterStatistics
            ]
        }

        if self._id is not None:
            character_dict["_id"] = str(self._id)

        return character_dict
    
    @classmethod
    def from_dict(cls, data):
        character_statistics = [
            CharacterStatistics(
                level=stat["level"],
                health=stat["health"],
                attack=stat["attack"],
                xpToUpgrade=stat["xpToUpgrade"],
                goldToUpgrade=stat["goldToUpgrade"]
            ) for stat in data.get("characterStatistics", [])
        ]

        _id = str(data.get("_id", ObjectId()))

        return cls(
            name=data["name"],
            description=data["description"],
            backOfCardDescription=data["backOfCardDescription"],
            photoUrl=data["photoUrl"],
            soundEffect=data["soundEffect"],
            unlockedAt=data["unlockedAt"],
            abilityId=data.get("abilityId", None),
            characterStatistics=character_statistics,
            _id=_id
        )
    
    def to_dict_for_update(self):
        character_dict = {
            key: value
            for key, value in self.to_dict().items()
            if key != '_id' and value is not None
        }
        return character_dict