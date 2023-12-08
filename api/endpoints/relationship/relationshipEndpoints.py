from flask import request, jsonify
from constants import RelationshipStatus
from models.relationship import Relationship
from .relationshipModel import RelationshipModel
import logging

class RelationshipEndpoints:
    def __init__(self, db):
        self.collection = db['relationships']
        self.relationshipModel = RelationshipModel(db)
        self.relationshipStatistics = []
    
    def get_relationship_by_user_ids(self, user1, user2):
        relationship = self.relationshipModel.get_relationship_by_user_ids(user1, user2)
        if relationship:
            return relationship.from_dict(relationship).to_dict()
        else:
            return {"message": "relationship not found"}, 404

    def create_or_update_relationship(self, data):
        user1 = data.get("user1")
        user2 = data.get("user2")
        relationshipStatus = data.get("relationshipStatus")
        try:
            relationship = self.relationshipModel.get_relationship_by_user_ids(user1, user2)
            if relationship:
                relationshipStatusEnum = RelationshipStatus[relationshipStatus]
                relationship.relationshipStatus = relationshipStatusEnum
                self.relationshipModel.update_relationship_status(relationship)

                return {"message": "relationship updated successfully"}, 200
            else:
                self.create_relationship(user1, user2, relationshipStatus)

        except Exception as e:
            return {"message": f"Failed to create or update relationship: {str(e)}"}, 500

    def create_relationship(self, user1, user2, relationshipStatus):
        try:
            relationship = Relationship(
                initiatingUserId=user1,
                receivingUserId=user2,
                relationshipStatus=relationshipStatus
            )

            relationshipId = self.relationshipModel.create_relationship(relationship)
            return {"relationshipId": relationshipId}, 201
        except Exception as e:
            logging.error(f"Failed to create relationship: {str(e)}")
            return {"message": f"Failed to create relationship: {str(e)}"}, 500
    
    def delete_relationship(self, user1, user2):
        try:
            relationship = self.relationshipModel.get_relationship_by_user_ids(user1, user2)
            if relationship:
                self.relationshipModel.delete_relationship(relationship['_id'])
                return {"message": "relationship deleted successfully"}, 204
            else:
                return {"message": "relationship not found or delete failed"}, 404

        except Exception as e:
            return {"message": f"Failed to delete relationship: {str(e)}"}, 500
    
    def get_all_relationships_by_status(self, data):
        userId = data.get("userId")
        relationshipStatus = data.get("relationshipStatus")
        try:
            relationships = self.relationshipModel.get_all_relationships_by_status(userId, relationshipStatus)
            relationship_instances = [relationship.from_dict(relationship) for relationship in relationships]
            return jsonify([relationship.to_dict() for relationship in relationship_instances])

        except Exception as e:
            return {"message": f"Failed to retrieve relationships: {str(e)}"}, 500
        