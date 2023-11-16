from flask import request, jsonify
from models.character import Character, CharacterStatistics
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
            return Character.from_dict(character).to_dict()
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
            id = data.get('id')
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

            self.update_statistics(character_statistics_list)

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

            if self.characterModel.update_character(id, character):
                return {"message": "Character updated successfully"}, 200
            else:
                return {"message": "Character not found or update failed"}, 404

        except Exception as e:
            return {"message": f"Failed to update character: {str(e)}"}, 500
        
    def update_statistics(self, new_stats):
        logging.debug(new_stats)
        for new_stat in new_stats:
            existing_stat = next(
                (stat for stat in self.characterStatistics if stat.level == new_stat.level),
                None
            )

            if existing_stat:
                existing_stat.health = new_stat.health
                existing_stat.attack = new_stat.attack
                existing_stat.xpToUpgrade = new_stat.xpToUpgrade
                existing_stat.goldToUpgrade = new_stat.goldToUpgrade
            else:
                self.characterStatistics.append(new_stat)

    def create_character(self, data):
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

            characterId = self.characterModel.create_character(character)
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
            logging.debug(characters)
            return jsonify([Character(**character).to_dict() for character in characters])

        except Exception as e:
            return {"message": f"Failed to retrieve characters: {str(e)}"}, 500