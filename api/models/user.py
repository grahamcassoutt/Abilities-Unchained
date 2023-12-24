from pymongo import MongoClient
from bson import ObjectId

class CharacterOwned:
    def __init__(self, characterId, level, currentXp, abilityStats = None):
        self.characterId = characterId
        self.level = level
        self.currentXp = currentXp
        self.abilityStats = abilityStats

    def to_dict(self):
        return {
            "characterId": self.characterId,
            "level": self.level,
            "currentXp": self.currentXp
        }
    
class AbilityStats:
    def __init__(self, abilityId, level, currentXp):
        self.abilityId = abilityId
        self.level = level
        self.currentXp = currentXp

class Chest:
    def __init__(self, userChestId, chestId, timeLeft, isActive):
        self.userChestId = userChestId
        self.chestId = chestId
        self.timeLeft = timeLeft
        self.isActive = isActive

    def to_dict(self):
        return {
            "userChestId": self.userChestId,
            "chestId": self.chestId,
            "timeLeft": self.timeLeft,
            "isActive": self.isActive
        }

class User:
    def __init__(self, username, email, displayName, isActive, level, xp, hitpoints, trophies, gold, wins, charactersOwned, abilityCardsSelected, nonAbilityCardsSelected, chests, game = None, _id=None):
        self._id = _id
        self.username = username
        self.email = email
        self.displayName = displayName
        self.isActive = isActive
        self.level = level
        self.xp = xp
        self.hitpoints = hitpoints
        self.trophies = trophies
        self.gold = gold
        self.wins = wins
        self.charactersOwned = charactersOwned
        self.abilityCardsSelected = abilityCardsSelected
        self.nonAbilityCardsSelected = nonAbilityCardsSelected
        self.game = game
        self.chests = chests

    def to_dict(self):
        user_dict = {
            "_id": ObjectId(),
            "username": self.username,
            "email": self.email,
            "displayName": self.displayName,
            "isActive": self.isActive,
            "level": self.level,
            "xp": self.xp,
            "hitpoints": self.hitpoints,
            "trophies": self.trophies,
            "gold": self.gold,
            "wins": self.wins,
            "charactersOwned": [
                {
                    "characterId": character.characterId,
                    "level": character.level,
                    "currentXp": character.currentXp,
                    "abilityStats": {
                        "abilityId": character.abilityStats.abilityId,
                        "level": character.abilityStats.level,
                        "currentXp": character.abilityStats.currentXp
                    } if character.abilityStats else None
                }
                for character in self.charactersOwned
            ],
            "abilityCardsSelected": [
                {
                    "characterId": character.characterId,
                    "level": character.level,
                    "currentXp": character.currentXp
                }
                for character in self.abilityCardsSelected
            ],
            "nonAbilityCardsSelected": [
                {
                    "characterId": character.characterId,
                    "level": character.level,
                    "currentXp": character.currentXp
                }
                for character in self.nonAbilityCardsSelected
            ],
            "chests": {
                "maxCount": self.chests['maxCount'],
                "currCount": self.chests['currCount'],
                "chest": [
                    {
                        "userChestId": chest.userChestId,
                        "chestId": chest.chestId,
                        "timeLeft": chest.timeLeft,
                        "isActive": chest.isActive
                    }
                    for chest in self.chests['chest']
                ]
            }
        }

        if self._id is not None:
            user_dict["_id"] = str(self._id)

        return user_dict
    
    @classmethod
    def from_dict(cls, json_data):
        characters_owned = [
            CharacterOwned(
                characterId=char['characterId'],
                level=char['level'],
                currentXp=char['currentXp'],
                abilityStats=AbilityStats(
                    abilityId=char['abilityStats']['abilityId'],
                    level=char['abilityStats']['level'],
                    currentXp=char['abilityStats']['currentXp']
                ) if char['abilityStats'] else None
            )
            for char in json_data.get('charactersOwned', [])
        ]

        abilityCardsSelected = [
            CharacterOwned(
                characterId=char['characterId'],
                level=char['level'],
                currentXp=char['currentXp']
            )
            for char in json_data.get('abilityCardsSelected', [])
        ]

        nonAbilityCardsSelected = [
            CharacterOwned(
                characterId=char['characterId'],
                level=char['level'],
                currentXp=char['currentXp']
            )
            for char in json_data.get('nonAbilityCardsSelected', [])
        ]

        chests = {
            "maxCount": json_data.get('chests', {}).get('maxCount'),
            "currCount": json_data.get('chests', {}).get('currCount'),
            "chest": [
                Chest(
                    userChestId=chest['userChestId'],
                    chestId=chest['chestId'],
                    timeLeft=chest['timeLeft'],
                    isActive=chest['isActive']
                )
                for chest in json_data.get('chests', {}).get('chest', [])
            ]
        }

        _id = str(json_data.get("_id", ObjectId()))

        return cls(
            _id=_id,
            username=json_data['username'],
            email=json_data['email'],
            displayName=json_data['displayName'],
            isActive=json_data['isActive'],
            level=json_data['level'],
            xp=json_data['xp'],
            hitpoints=json_data['hitpoints'],
            trophies=json_data['trophies'],
            gold=json_data['gold'],
            wins=json_data['wins'],
            charactersOwned=characters_owned,
            abilityCardsSelected=abilityCardsSelected,
            nonAbilityCardsSelected=nonAbilityCardsSelected,
            chests=chests
        )