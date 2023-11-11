from flask import request, jsonify
from models.character import Character, CharacterStatistics
from characterModel import CharacterModel
import logging

class CharacterEndpoints:
    def get(self, character_id):
        character = CharacterModel.get_character(character_id)
        if character:
            return jsonify(Character(**character).to_dict())
        else:
            return {"message": "Character not found"}, 404

    def put(self, characterId):
        try:
            data = request.get_json()
            character_statistics_data = data.get("characterStatistics", [])

            character_statistics_list = [
                CharacterStatistics(
                    level=stat_data.get("level"),
                    health=stat_data.get("health"),
                    attack=stat_data.get("attack"),
                    xp_to_upgrade=stat_data.get("xpToUpgrade"),
                    gold_to_upgrade=stat_data.get("goldToUpgrade")
                ) for stat_data in character_statistics_data
            ]

            character = Character(
                name=data.get("name"),
                description=data.get("description"),
                back_of_card_description=data.get("backOfCardDescription"),
                photo_url=data.get("photoUrl"),
                sound_effect=data.get("soundEffect"),
                unlocked_at=data.get("unlockedAt"),
                ability_id=data.get("abilityId"),
                character_statistics=character_statistics_list
            )

            if CharacterModel.update_character(characterId, character):
                return {"message": "Character updated successfully"}, 200
            else:
                return {"message": "Character not found or update failed"}, 404

        except Exception as e:
            return {"message": f"Failed to update character: {str(e)}"}, 500

    def post(self):
        data = request.get_json()

        logging.debug("Got data")

        if not data:
            return {"message": "No data provided in the request"}, 400

        try:
            character_statistics_data = data.get("characterStatistics", [])

            character_statistics_list = [
                CharacterStatistics(
                    level=stat_data.get("level"),
                    health=stat_data.get("health"),
                    attack=stat_data.get("attack"),
                    xp_to_upgrade=stat_data.get("xpToUpgrade"),
                    gold_to_upgrade=stat_data.get("goldToUpgrade")
                ) for stat_data in character_statistics_data
            ]

            character = Character(
                name=data.get("name"),
                description=data.get("description"),
                back_of_card_description=data.get("backOfCardDescription"),
                photo_url=data.get("photoUrl"),
                sound_effect=data.get("soundEffect"),
                unlocked_at=data.get("unlockedAt"),
                ability_id=data.get("abilityId"),
                character_statistics=character_statistics_list
            )

            character_id = CharacterModel.create_character(character)
            return {"character_id": character_id}, 201
        except Exception as e:
            logging.error(f"Failed to create character: {str(e)}")
            return {"message": f"Failed to create character: {str(e)}"}, 500
    
    def delete(self, characterId):
        try:
            if CharacterModel.delete_character(characterId):
                return {"message": "Character deleted successfully"}, 204
            else:
                return {"message": "Character not found or delete failed"}, 404

        except Exception as e:
            return {"message": f"Failed to delete character: {str(e)}"}, 500
    
    def get_all(self):
        try:
            characters = CharacterModel.get_all_characters()
            return jsonify([Character(**character).to_dict() for character in characters])

        except Exception as e:
            return {"message": f"Failed to retrieve characters: {str(e)}"}, 500