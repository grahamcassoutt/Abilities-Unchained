import logging
import pymongo
from bson.objectid import ObjectId

class userModel:
    def __init__(self, db):
        self.collection = db['users']

    def create_user(self, user):
        user_document = user.to_dict()
        logging.debug(user_document)
        result = self.collection.insert_one(user_document)
        return str(result.inserted_id)

    def get_user_by_id(self, userId):
        user = self.collection.find_one({"_id": userId})
        return user

    def update_user(self, userId, user):
        result = self.collection.update_one({"_id": userId}, {"$set": user})
        if result.modified_count > 0:
            logging.debug("Update successful")
        else:
            logging.error(f"Update failed: {result.raw_result}")
        return result.modified_count > 0

    def delete_user(self, userId):
        result = self.collection.delete_one({"_id": ObjectId(userId)})
        return result.deleted_count > 0
    
    