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
    def __init__(self, name, description, back_of_card_description, photo_url, sound_effect, unlocked_at, ability_id, character_statistics):
        self.name = name
        self.description = description
        self.back_of_card_description = back_of_card_description
        self.photo_url = photo_url
        self.sound_effect = sound_effect
        self.unlocked_at = unlocked_at
        self.ability_id = ability_id
        self.character_statistics = character_statistics

    def to_dict(self):
        return {
            "_id": ObjectId(),
            "name": self.name,
            "description": self.description,
            "back_of_card_description": self.back_of_card_description,
            "photo_url": self.photo_url,
            "sound_effect": self.sound_effect,
            "unlocked_at": self.unlocked_at,
            "ability_id": self.ability_id if self.ability_id else None, #Optional
            "character_statistics": [
                {
                    "level": stat.level,
                    "health": stat.health,
                    "attack": stat.attack,
                    "xp_to_upgrade": stat.xp_to_upgrade,
                    "gold_to_upgrade": stat.gold_to_upgrade
                }
                for stat in self.character_statistics
            ]
        }
