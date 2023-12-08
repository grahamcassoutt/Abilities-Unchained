import logging
import pymongo
from bson.objectid import ObjectId

class ChestModel:
    def __init__(self, db):
        self.collection = db['chests']

    def create_chest(self, chest):
        chest_document = chest.to_dict()
        logging.debug(chest_document)
        result = self.collection.insert_one(chest_document)
        return str(result.inserted_id)

    def get_chest_by_id(self, chestId):
        chest = self.collection.find_one({"_id": ObjectId(chestId)})
        return chest

    def update_chest(self, chestId, chest):
        chest_document = chest.to_dict_for_update()
        result = self.collection.update_one({"_id": ObjectId(chestId)}, {"$set": chest_document})
        if result.modified_count > 0:
            logging.debug("Update successful")
        else:
            logging.error(f"Update failed: {result.raw_result}")
        return result.modified_count > 0

    def delete_chest(self, chestId):
        result = self.collection.delete_one({"_id": ObjectId(chestId)})
        return result.deleted_count > 0
