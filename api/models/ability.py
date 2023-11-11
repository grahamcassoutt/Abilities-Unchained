import pymongo
from bson.objectid import ObjectId

class DeathDamage:
    def __init__(self, characters, hitPoints):
        self.characters = characters
        self.hitPoints = hitPoints

class Poison:
    def __init__(self, numberOfTurns, damage, reusable):
        self.numberOfTurns = numberOfTurns
        self.damage = damage
        self.reusable = reusable

class ChargedBoom:
    def __init__(self, numRoundsBetweenBoom, multiplier):
        self.numRoundsBetweenBoom = numRoundsBetweenBoom
        self.multiplier = multiplier

class Sacrifice:
    def __init__(self, damageToCharacters, damageToHP):
        self.damageToCharacters = damageToCharacters
        self.damageToHP = damageToHP

class AbilityStatistics:
    def __init__(self, level, oppHP, thisCharacterAtt, yourSideDef, deathDamage, poison, chargedBoom, sacrifice):
        self.level = level
        self.oppHP = oppHP
        self.thisCharacterAtt = thisCharacterAtt
        self.yourSideDef = yourSideDef
        self.deathDamage = deathDamage
        self.poison = poison
        self.chargedBoom = chargedBoom
        self.sacrifice = sacrifice

class Ability:
    def __init__(self, name, description, icon, visualEffect, abilityStatistics):
        self.name = name
        self.description = description
        self.icon = icon
        self.visualEffect = visualEffect
        self.abilityStatistics = abilityStatistics

    def to_json(self):
        return {
            "_id": ObjectId(),
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "icon": self.icon,
            "visualEffect": self.visualEffect,
            "abilityStatistics": [
                {
                    "level": stats.level,
                    "oppHP": stats.oppHP,
                    "thisCharacterAtt": stats.thisCharacterAtt,
                    "yourSideDef": stats.yourSideDef,
                    "deathDamage": {
                        "characters": stats.deathDamage.characters,
                        "hitPoints": stats.deathDamage.hitPoints
                    } if stats.deathDamage else None,
                    "poison": {
                        "numberOfTurns": stats.poison.numberOfTurns,
                        "damage": stats.poison.damage,
                        "reusable": stats.poison.reusable
                    } if stats.poison else None,
                    "chargedBoom": {
                        "numRoundsBetweenBoom": stats.chargedBoom.numRoundsBetweenBoom,
                        "multiplier": stats.chargedBoom.multiplier
                    } if stats.chargedBoom else None,
                    "sacrifice": {
                        "damageToCharacters": stats.sacrifice.damageToCharacters,
                        "damageToHP": stats.sacrifice.damageToHP
                    } if stats.sacrifice else None
                }
                for stats in self.abilityStatistics
            ]
        }
    
# Example creation of Ability
# ability = Ability(
#     id=1,
#     name="Some Ability",
#     description="Description of the ability",
#     icon="path/to/icon.png",
#     visualEffect="path/to/effect.png",
#     abilityStatistics=[
#         AbilityStatistics(
#             level=1,
#             oppHP=100,
#             thisCharacterAtt=50,
#             yourSideDef=20,
#             deathDamage=DeathDamage(characters=2, hitPoints=10),
#             poison=Poison(numberOfTurns=3, damage=5, reusable=True),
#             chargedBoom=ChargedBoom(numRoundsBetweenBoom=2, multiplier=3),
#             sacrifice=Sacrifice(damageToCharacters=20, damageToHP=15)
#         ),
#         AbilityStatistics(
#             level=2,
#             oppHP=120,
#             thisCharacterAtt=60,
#             yourSideDef=25,
#             deathDamage=None,
#             poison=None,
#             chargedBoom=None,
#             sacrifice=None
#         )
#     ]
# )