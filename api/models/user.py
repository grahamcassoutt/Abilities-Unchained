from pymongo import MongoClient
from bson import ObjectId

class CharacterInGame:
    def __init__(self, characterId, level, isAlive):
        self.characterId = characterId
        self.level = level
        self.isAlive = isAlive

class CharacterOwned:
    def __init__(self, characterId, level, currentXp):
        self.characterId = characterId
        self.level = level
        self.currentXp = currentXp

class Chest:
    def __init__(self, chestObject, timeLeft, isActive):
        self.chestObject = chestObject
        self.timeLeft = timeLeft
        self.isActive = isActive

class User:
    def __init__(self, username, email, displayName, isActive, level, xp, hitpoints, trophies, gold, wins, charactersOwned, game, chests):
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
        self.game = game
        self.chests = chests

    def to_json(self):
        return {
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
                    "currentXp": character.currentXp
                }
                for character in self.charactersOwned
            ],
            "game": {
                "cardsChosen": [
                    {
                        "characterId": card.characterId,
                        "level": card.level,
                        "isAlive": card.isAlive
                    }
                    for card in self.game['cardsChosen']
                ],
                "charactersOnBoard": [
                    {
                        "attack": character.attack,
                        "defense": character.defense
                    }
                    for character in self.game['charactersOnBoard']
                ],
                "hitPoints": self.game['hitPoints']
            },
            "chests": {
                "maxCount": self.chests['maxCount'],
                "currCount": self.chests['currCount'],
                "chest": [
                    {
                        "chestObject": chest.chestObject,
                        "timeLeft": chest.timeLeft.isoformat() if chest.timeLeft else None,
                        "isActive": chest.isActive
                    }
                    for chest in self.chests['chest']
                ]
            }
        }