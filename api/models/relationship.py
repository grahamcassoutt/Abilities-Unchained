from pymongo import MongoClient
from bson import ObjectId
from constants import RelationshipStatus

class Relationship:
    def __init__(self, initiatingUserId, receivingUserId, relationshipStatus, _id=None):
        self._id = _id
        self.initiatingUserId = initiatingUserId
        self.receivingUserId = receivingUserId
        self.relationshipStatus = relationshipStatus

    def to_dict(self):
        relationship_dict = {
            "_id": ObjectId(),
            "initiatingUserId": self.initiatingUserId,
            "receivingUserId": self.receivingUserId,
            "relationshipStatus": RelationshipStatus(self.relationshipStatus).name
        }

        if self._id is not None:
            relationship_dict["_id"] = str(self._id)

        return relationship_dict
    
    @classmethod
    def from_dict(cls, relationship_dict):
        initiating_user_id = relationship_dict['initiatingUserId']
        receiving_user_id = relationship_dict['receivingUserId']
        relationship_status = RelationshipStatus[relationship_dict['relationshipStatus']]

        _id = str(relationship_dict.get("_id", ObjectId()))

        return cls(initiating_user_id, receiving_user_id, relationship_status, _id)

