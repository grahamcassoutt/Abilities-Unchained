import logging
import pymongo
from bson.objectid import ObjectId

class RelationshipModel:
    def __init__(self, db):
        self.collection = db['relationships']

    def create_relationship(self, relationship):
        relationship_document = relationship.to_dict()
        logging.debug(relationship_document)
        result = self.collection.insert_one(relationship_document)
        return str(result.inserted_id)

    def get_relationship_by_user_ids(self, userId1, userId2):
        relationship = self.collection.find_one({
            "$or": [
                {"initiatingUserId": userId1, "receivingUserId": userId2},
                {"initiatingUserId": userId2, "receivingUserId": userId1}
            ]
        })
        return relationship

    def update_relationship_status(self, relationship):
        result = self.collection.update_one(
            {"_id": ObjectId(relationship['_id'])},
            {"$set": {"relationshipStatus": relationship.relationshipStatus.name}}
        )
        
        if result.modified_count > 0:
            logging.debug("Update successful")
        else:
            logging.error(f"Update failed: {result.raw_result}")
        
        return result.modified_count > 0


    def delete_relationship(self, relationshipId):
        result = self.collection.delete_one({"_id": ObjectId(relationshipId)})
        return result.deleted_count > 0
    
    def get_all_relationships_by_status(self, userId, relationshipStatus):
        relationships = list(self.collection.find({"relationshipStatus": relationshipStatus}))
        relationships = list(self.collection.find({
            "$and": [
                {
                    "$or": [
                        {"initiatingUserId": userId},
                        {"receivingUserId": userId}
                    ]
                },
                {"relationshipStatus": relationshipStatus}
            ]
        }))
        return relationships
