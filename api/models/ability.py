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
    def __init__(self, level, oppHP, attGainedWhenLoseHP, yourSideDef, deathDamage = None, poison = None, chargedBoom = None, sacrifice = None):
        self.level = level
        self.oppHP = oppHP
        self.attGainedWhenLoseHP = attGainedWhenLoseHP
        self.yourSideDef = yourSideDef
        self.deathDamage = deathDamage
        self.poison = poison
        self.chargedBoom = chargedBoom
        self.sacrifice = sacrifice

class Ability:
    def __init__(self, name, description, icon, visualEffect, abilityStatistics, _id = None):
        self._id = _id
        self.name = name
        self.description = description
        self.icon = icon
        self.visualEffect = visualEffect
        self.abilityStatistics = abilityStatistics

    def to_dict(self):
        ability_dict = {
            "name": self.name,
            "description": self.description,
            "icon": self.icon,
            "visualEffect": self.visualEffect,
            "abilityStatistics": [
                {
                    "level": stats.level,
                    "oppHP": stats.oppHP,
                    "attGainedWhenLoseHP": stats.attGainedWhenLoseHP,
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

        if self._id is not None:
            ability_dict["_id"] = str(self._id)

        return ability_dict
    
    @classmethod
    def from_dict(cls, data):
        poison = [
            Poison(
                numberOfTurns=stat['poison']['numberOfTurns'],
                damage=stat['poison']['damage'],
                reusable=stat['poison']['reusable']
            ) if 'poison' in stat and stat['poison'] is not None else None
            for stat in data.get('abilityStatistics', [])
        ]

        death_damage = [
            DeathDamage(
                characters=stat['deathDamage']['characters'],
                hitPoints=stat['deathDamage']['hitPoints']
            ) if 'deathDamage' in stat and stat['deathDamage'] is not None else None
            for stat in data.get('abilityStatistics', [])
        ]

        charged_boom = [
            ChargedBoom(
                numRoundsBetweenBoom=stat['chargedBoom']['numRoundsBetweenBoom'],
                multiplier=stat['chargedBoom']['multiplier']
            ) if 'chargedBoom' in stat and stat['chargedBoom'] is not None else None
            for stat in data.get('abilityStatistics', [])
        ]

        sacrifice = [
            Sacrifice(
                damageToCharacters=stat['sacrifice']['damageToCharacters'],
                damageToHP=stat['sacrifice']['damageToHP']
            ) if 'sacrifice' in stat and stat['sacrifice'] is not None else None
            for stat in data.get('abilityStatistics', [])
        ]

        ability_statistics = [
            AbilityStatistics(
                level=stat['level'],
                oppHP=stat['oppHP'],
                attGainedWhenLoseHP=stat['attGainedWhenLoseHP'],
                yourSideDef=stat['yourSideDef'],
                deathDamage=death_damage[i],
                poison=poison[i],
                chargedBoom=charged_boom[i],
                sacrifice=sacrifice[i]
            ) for i, stat in enumerate(data.get("abilityStatistics", []))
        ]

        _id = str(data.get("_id", ObjectId()))

        return cls(
            name=data['name'],
            description=data['description'],
            icon=data['icon'],
            visualEffect=data['visualEffect'],
            abilityStatistics=ability_statistics,
            _id=_id
        )
