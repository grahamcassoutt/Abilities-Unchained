from flask import request, jsonify
from models.ability import Ability
from .abilityModel import AbilityModel
import logging

class AbilityEndpoints:
    def __init__(self, db):
        self.collection = db['Abilities']
        self.abilityModel = AbilityModel(db)
    
    def get_ability_by_id(self, abilityId):
        ability = self.abilityModel.get_ability_by_id(abilityId)
        if ability:
            return Ability.from_dict(ability)
        else:
            return {"message": "ability not found"}, 404

    def create_or_update_ability(self):
        data = request.get_json()

        if 'id' in data:
            return self.update_ability(data)
        else:
            return self.create_ability(data)

    def update_ability(self, data):
        try:
            ability = self.abilityModel.get_ability_by_id(data.get('id'))
            ability_statistics_data = data.get("abilityStatistics", [])

            ability = self.update_statistics(ability, ability_statistics_data)

            if self.abilityModel.update_ability(data.get('id'), ability):
                return {"message": "ability updated successfully"}, 200
            else:
                return {"message": "ability not found or update failed"}, 404

        except Exception as e:
            return {"message": f"Failed to update ability: {str(e)}"}, 500
        
    def update_statistics(self, ability, new_stats):
        for new_stat in new_stats:
            level = new_stat['level']
            existing_stat = next(
                (stat for stat in ability['abilityStatistics'] if stat['level'] == level),
                None
            )

            if existing_stat:
                existing_stat['oppHP'] = new_stat.get('oppHP', existing_stat['oppHP'])
                existing_stat['attGainedWhenLoseHP'] = new_stat.get('attGainedWhenLoseHP', existing_stat['attGainedWhenLoseHP'])
                existing_stat['yourSideDef'] = new_stat.get('yourSideDef', existing_stat['yourSideDef'])
                existing_stat['deathDamage'] = new_stat.get('deathDamage', existing_stat['deathDamage'])
                existing_stat['poison'] = new_stat.get('poison', existing_stat['poison'])
                existing_stat['chargedBoom'] = new_stat.get('chargedBoom', existing_stat['chargedBoom'])
                existing_stat['sacrifice'] = new_stat.get('sacrifice', existing_stat['sacrifice'])
            else:
                ability['abilityStatistics'].append(new_stat)

        return Ability.from_dict(ability).to_dict()

    def create_ability(self, data):
        if not data:
            return {"message": "No data provided in the request"}, 400

        try:
            abilityInstance = Ability.from_dict(data)
            abilityId = self.abilityModel.create_ability(abilityInstance)
            return {"abilityId": abilityId}, 201
        except Exception as e:
            logging.error(f"Failed to create ability: {str(e)}")
            return {"message": f"Failed to create ability: {str(e)}"}, 500
    
    def delete_ability(self, abilityId):
        try:
            if self.abilityModel.delete_ability(abilityId):
                return {"message": "ability deleted successfully"}, 204
            else:
                return {"message": "ability not found or delete failed"}, 404

        except Exception as e:
            return {"message": f"Failed to delete ability: {str(e)}"}, 500
        
    def get_all_abilities(self):
        try:
            abilities = self.abilityModel.get_all_abilities()
            ability_instances = [Ability.from_dict(ability) for ability in abilities]
            return jsonify([ability.to_dict() for ability in ability_instances])

        except Exception as e:
            return {"message": f"Failed to retrieve abilities: {str(e)}"}, 500

    def get_abilities_by_levels(self):
        try:
            data = request.get_json()
            abilitiesOneLevel = self.abilityModel.get_abilities_by_level(data)
            abilities_with_levels = [Ability.from_dict(ability).to_dict() for ability in abilitiesOneLevel]
            # abilities = []
            # for ability in abilities_with_levels:
            #     filtered_stats = []

            #     for stat in ability.get('abilityStatistics', []):
            #         filtered_stat = {
            #             key: value
            #             for key, value in stat.items()
            #             if value is not None and value != 0
            #         }

            #         filtered_stats.append(filtered_stat)
            #     ability['abilityStatistics'] = filtered_stats
            #     abilities.append(ability)
            return abilities_with_levels

        except Exception as e:
            return {"message": f"Failed to retrieve abilities: {str(e)}"}, 500