from pymongo import MongoClient
from bson import ObjectId
from constants import RelationshipStatus

class Relationship:
    def __init__(self, initiatingUserId, receivingUserId, relationshipStatus):
        self.initiatingUserId = initiatingUserId
        self.receivingUserId = receivingUserId
        self.relationshipStatus = relationshipStatus

    def to_json(self):
        return {
            "_id": ObjectId(),
            "initiatingUserId": self.initiatingUserId,
            "receivingUserId": self.receivingUserId,
            "relationshipStatus": RelationshipStatus(self.relationshipStatus).name
        }
