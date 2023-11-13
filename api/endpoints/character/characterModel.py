import pymongo
from bson.objectid import ObjectId

class CharacterModel:
    def __init__(self, db):
        self.collection = db['characters']

    def create_character(self, character):
        character_document = character.to_dict()
        result = self.collection.insert_one(character_document)
        return str(result.inserted_id)

    def get_character_by_id(self, character_id):
        character = self.collection.find_one({"_id": ObjectId(character_id)})
        return character

    def update_character(self, character_id, character):
        character_document = character.to_dict()
        result = self.collection.update_one({"_id": ObjectId(character_id)}, {"$set": character_document})
        return result.modified_count > 0

    def delete_character(self, character_id):
        result = self.collection.delete_one({"_id": ObjectId(character_id)})
        return result.deleted_count > 0
    
    def get_all_characters(self):
        characters = list(self.collection.find())
        return characters
