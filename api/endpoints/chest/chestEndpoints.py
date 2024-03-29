from flask import request, jsonify
from models.chest import Chest
from .chestModel import ChestModel
import logging

class ChestEndpoints:
    def __init__(self, db):
        self.collection = db['Chests']
        self.chestModel = ChestModel(db)
    
    def get_chest_by_id(self, chestId):
        chest = self.chestModel.get_chest_by_id(chestId)
        if chest:
            return Chest.from_dict(chest)
        else:
            return {"message": "Chest not found"}, 404

    def create_or_update_chest(self):
        data = request.get_json()

        if 'id' in data:
            return self.update_chest(data)
        else:
            return self.create_chest(data)

    def update_chest(self, data):
        try:
            chest = self.chestModel.get_chest_by_id(data.get('id'))
            chest.update(data)
            del chest['id']

            if self.chestModel.update_chest(data.get('id'), chest):
                return {"message": "Chest updated successfully"}, 200
            else:
                return {"message": "Chest not found or update failed"}, 404

        except Exception as e:
            return {"message": f"Failed to update chest: {str(e)}"}, 500

    def create_chest(self, data):
        if not data:
            return {"message": "No data provided in the request"}, 400

        try:
            chestInstance = Chest.from_dict(data)
            chestId = self.chestModel.create_chest(chestInstance)
            return {"chestId": chestId}, 201
        except Exception as e:
            logging.error(f"Failed to create chest: {str(e)}")
            return {"message": f"Failed to create chest: {str(e)}"}, 500
    
    def delete_chest(self, chestId):
        try:
            if self.chestModel.delete_chest(chestId):
                return {"message": "Chest deleted successfully"}, 204
            else:
                return {"message": "Chest not found or delete failed"}, 404

        except Exception as e:
            return {"message": f"Failed to delete chest: {str(e)}"}, 500
        