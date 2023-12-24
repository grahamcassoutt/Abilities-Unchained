import uuid
from flask import request
from models.user import User, Chest
from endpoints.chest.chestModel import ChestModel
from .userModel import userModel
import logging

class UserEndpoints:
    def __init__(self, db):
        self.collection = db['users']
        self.userModel = userModel(db)
        self.chestModel = ChestModel(db)
        self.userStatistics = []
    
    def get_user_by_id(self, userId):
        user = self.userModel.get_user_by_id(userId)
        if user:
            return User.from_dict(user)
        else:
            return {"message": "user not found"}, 404

    def update_user(self):
        try:
            data = request.get_json()
            user = self.userModel.get_user_by_id(data['id'])
            user.update(data)
            del user['_id']

            if self.userModel.update_user(data['id'], user):
                return {"message": "user updated successfully"}, 200
            else:
                return {"message": "user not found or update failed"}, 404

        except Exception as e:
            return {"message": f"Failed to update user: {str(e)}"}, 500

    def create_user(self):
        data = request.get_json()
        if not data:
            return {"message": "No data provided in the request"}, 400

        try:
            userInstance = User.from_dict(data)
            userId = self.userModel.create_user(userInstance)
            return {"userId": userId}, 201
        except Exception as e:
            logging.error(f"Failed to create user: {str(e)}")
            return {"message": f"Failed to create user: {str(e)}"}, 500
    
    def delete_user(self, userId):
        try:
            if self.userModel.delete_user(userId):
                return {"message": "user deleted successfully"}, 204
            else:
                return {"message": "user not found or delete failed"}, 404

        except Exception as e:
            return {"message": f"Failed to delete user: {str(e)}"}, 500
        

    def update_characters(self):
        try:
            data = request.get_json()
            user = self.userModel.get_user_by_id(data['id'])
            charactersToAdd = data.get('charactersOwned', [])
           
            user['charactersOwned'].extend(charactersToAdd)
            del user['_id']
            self.userModel.update_user(data['id'], user)
            return {"message": "Characters added successfully"}, 200
        except Exception as e:
            return {"message": f"Failed to add characters to user: {str(e)}"}, 500

    def update_chests(self):
        try:
            data = request.get_json()
            user = self.userModel.get_user_by_id(data['userId'])
            del user['_id']
            
            if data['add']:
                chest = self.chestModel.get_chest_by_id(data['chestId'])
                user['chests']['currCount'] += 1
                user['chests']['chest'].append(Chest(
                    userChestId=str(uuid.uuid4()),
                    chestId=chest['_id'],
                    timeLeft=chest['timeToOpen'],
                    isActive=False
                ).to_dict())
            else:
                user['chests']['currCount'] -= 1
                user['chests']['chest'] = [chest for chest in user['chests']['chest'] if chest.get('userChestId') != data['userChestId']]

            self.userModel.update_user(data['userId'], user)
            return {"message": "Chests modified successfully"}, 200
        except Exception as e:
            return {"message": f"Failed to update user chests: {str(e)}"}, 500

    def swap_chosen_cards(self):
        try:
            data = request.get_json()
            user = self.userModel.get_user_by_id(data['userId'])
            del user['_id']
            
            if data['ability']:
                chosen = self.swap(user['abilityCardsSelected'], data['cardToAdd'], data['cardIdToRemove']) 
                user['abilityCardsSelected'] = chosen               
            else:
                chosen = self.swap(user['nonAbilityCardsSelected'], data['cardToAdd'], data['cardIdToRemove']) 
                user['nonAbilityCardsSelected'] = chosen 
                
            self.userModel.update_user(data['userId'], user)
            return {"message": "Card swapped successfully"}, 200
        except Exception as e:
            return {"message": f"Failed to swap selected card: {str(e)}"}, 500
    
    def swap(self, givenList, cardToAdd, cardIdToRemove = ""):
        if cardIdToRemove == "":
            givenList.append(cardToAdd)
            return givenList
        filtered_list = [item for item in givenList if item["characterId"] != cardIdToRemove]
        filtered_list.append(cardToAdd)
        return filtered_list
        
