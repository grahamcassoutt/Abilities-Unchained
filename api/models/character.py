import pymongo
from bson.objectid import ObjectId

class CharacterStatistics:
    def __init__(self, level, health, attack, xp_to_upgrade, gold_to_upgrade):
        self.level = level
        self.health = health
        self.attack = attack
        self.xp_to_upgrade = xp_to_upgrade
        self.gold_to_upgrade = gold_to_upgrade

class Character:
    def __init__(self, name, description, back_of_card_description, photo_url, sound_effect, unlocked_at, ability_id, character_statistics, _id = None):
        self._id = _id
        self.name = name
        self.description = description
        self.back_of_card_description = back_of_card_description
        self.photo_url = photo_url
        self.sound_effect = sound_effect
        self.unlocked_at = unlocked_at
        self.ability_id = ability_id
        self.character_statistics = character_statistics

    def to_dict(self):
        character_dict = {
            "name": self.name,
            "description": self.description,
            "backOfCardDescription": self.back_of_card_description,
            "photoUrl": self.photo_url,
            "soundEffect": self.sound_effect,
            "unlockedAt": self.unlocked_at,
            "abilityId": self.ability_id if self.ability_id else None,
            "characterStatistics": [
                {
                    "level": stat.level,
                    "health": stat.health,
                    "attack": stat.attack,
                    "xpToUpgrade": stat.xp_to_upgrade,
                    "goldToUpgrade": stat.gold_to_upgrade
                }
                for stat in self.character_statistics
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
                xp_to_upgrade=stat["xpToUpgrade"],
                gold_to_upgrade=stat["goldToUpgrade"]
            ) for stat in data.get("characterStatistics", [])
        ]

        _id = str(data.get("_id", ObjectId()))

        return cls(
            name=data["name"],
            description=data["description"],
            back_of_card_description=data["backOfCardDescription"],
            photo_url=data["photoUrl"],
            sound_effect=data["soundEffect"],
            unlocked_at=data["unlockedAt"],
            ability_id=data.get("abilityId"),
            character_statistics=character_statistics,
            _id=_id
        )
    
    def to_dict_for_update(self):
        character_dict = {
            key: value
            for key, value in self.to_dict().items()
            if key != '_id' and value is not None
        }
        return character_dict