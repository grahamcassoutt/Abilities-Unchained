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
        character = self.collection.find_one({"_id": ObjectId(characterId)})
        return character

    def update_character(self, characterId, character):
        character_document = character.to_dict_for_update()
        result = self.collection.update_one({"_id": ObjectId(characterId)}, {"$set": character_document})
        if result.modified_count > 0:
            logging.debug("Update successful")
        else:
            logging.error(f"Update failed: {result.raw_result}")
        return result.modified_count > 0

    def delete_character(self, characterId):
        result = self.collection.delete_one({"_id": ObjectId(characterId)})
        return result.deleted_count > 0
    
    def get_all_characters(self):
        characters = list(self.collection.find())
        return characters
