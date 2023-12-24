from flask import request, jsonify
from models.character import Character
from .characterModel import CharacterModel
import logging

class CharacterEndpoints:
    def __init__(self, db):
        self.collection = db['Characters']
        self.characterModel = CharacterModel(db)
        self.characterStatistics = []
    
    def get_character_by_id(self, characterId):
        character = self.characterModel.get_character_by_id(characterId)
        if character:
            return Character.from_dict(character)
        else:
            return {"message": "Character not found"}, 404

    def create_or_update_character(self):
        data = request.get_json()

        if 'id' in data:
            return self.update_character(data)
        else:
            return self.create_character(data)

    def update_character(self, data):
        try:
            character = self.characterModel.get_character_by_id(data.get('id'))
            character_statistics_data = data.get("characterStatistics", [])
            character = self.update_statistics(character, character_statistics_data)

            if self.characterModel.update_character(data.get('id'), character):
                return {"message": "Character updated successfully"}, 200
            else:
                return {"message": "Character not found or update failed"}, 404

        except Exception as e:
            return {"message": f"Failed to update character: {str(e)}"}, 500
        
    def update_statistics(self, character, new_stats):
        for new_stat in new_stats:
            level = new_stat['level']
            existing_stat = next(
                (stat for stat in character['characterStatistics'] if stat['level'] == level),
                None
            )

            if existing_stat:
                existing_stat['health'] = new_stat.get('health', existing_stat['health'])
                existing_stat['attack'] = new_stat.get('attack', existing_stat['attack'])
                existing_stat['xpToUpgrade'] = new_stat.get('xpToUpgrade', existing_stat['xpToUpgrade'])
                existing_stat['goldToUpgrade'] = new_stat.get('goldToUpgrade', existing_stat['goldToUpgrade'])
            else:
                character['characterStatistics'].append(new_stat)

        return character

    def create_character(self, data):
        if not data:
            return {"message": "No data provided in the request"}, 400

        try:
            characterInstance = Character.from_dict(data)
            characterId = self.characterModel.create_character(characterInstance)
            return {"characterId": characterId}, 201
        except Exception as e:
            logging.error(f"Failed to create character: {str(e)}")
            return {"message": f"Failed to create character: {str(e)}"}, 500
    
    def delete_character(self, characterId):
        try:
            if self.characterModel.delete_character(characterId):
                return {"message": "Character deleted successfully"}, 204
            else:
                return {"message": "Character not found or delete failed"}, 404

        except Exception as e:
            return {"message": f"Failed to delete character: {str(e)}"}, 500
    
    def get_all_characters(self):
        try:
            characters = self.characterModel.get_all_characters()
            character_instances = [Character.from_dict(character) for character in characters]
            return jsonify([character.to_dict() for character in character_instances])

        except Exception as e:
            return {"message": f"Failed to retrieve characters: {str(e)}"}, 500
        
    def get_characters_by_levels_specific(self, hasAbility):
        try:
            data = request.get_json()
            characters_with_levels = []
            charactersOneLevel = self.characterModel.get_characters_by_level(data, hasAbility)
            characters_with_levels = [Character.from_dict(character).to_dict() for character in charactersOneLevel]
            return characters_with_levels

        except Exception as e:
            return {"message": f"Failed to retrieve characters: {str(e)}"}, 500

    def get_characters_by_levels(self):
        try:
            data = request.get_json()
            characters_with_levels = []
            charactersOneLevel = self.characterModel.get_characters_by_level(data)
            characters_with_levels = [Character.from_dict(character).to_dict() for character in charactersOneLevel]
            return characters_with_levels

        except Exception as e:
            return {"message": f"Failed to retrieve characters: {str(e)}"}, 500

