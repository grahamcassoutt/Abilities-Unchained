import logging
import pymongo
from bson.objectid import ObjectId

class CharacterModel:
    def __init__(self, db):
        self.collection = db['characters']

    def create_character(self, character):
        character_document = character.to_dict()
        logging.debug(character_document)
        result = self.collection.insert_one(character_document)
        return str(result.inserted_id)

    def get_character_by_id(self, characterId):
        character = self.collection.find_one({"_id": characterId})
        return character

    def update_character(self, characterId, character):
        result = self.collection.update_one({"_id": characterId}, {"$set": character})
        if result.modified_count > 0:
            logging.debug("Update successful")
        else:
            logging.error(f"Update failed: {result.raw_result}")
        return result.modified_count > 0

    def delete_character(self, characterId):
        result = self.collection.delete_one({"_id": characterId})
        return result.deleted_count > 0
    
    def get_all_characters(self):
        return list(self.collection.find())

    def get_characters_by_level(self, data):
        for req in data:
            req['characterId'] = ObjectId(req['characterId'])

        return self.collection.aggregate([
            {
                '$match': {'_id': {'$in': [req['characterId'] for req in data]}}
            },
            {
                '$project': {
                    '_id': 1,
                    'name': 1,
                    'description': 1,
                    'backOfCardDescription': 1,
                    'photoUrl': 1,
                    'soundEffect': 1,
                    'unlockedAt': 1,
                    'abilityId': 1,
                    'characterStatistics': {
                        '$filter': {
                            'input': '$characterStatistics',
                            'as': 'stat',
                            'cond': {'$eq': ['$$stat.level', {'$arrayElemAt': [{'$map': {'input': data, 'as': 'd', 'in': '$$d.level'}}, {'$indexOfArray': [{'$map': {'input': data, 'as': 'd', 'in': '$$d.characterId'}}, '$_id']}]}]}
                        }
                    }
                }
            }
        ])