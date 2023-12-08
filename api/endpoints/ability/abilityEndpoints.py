from flask import request, jsonify
from models.ability import Ability, AbilityStatistics
from .abilityModel import AbilityModel
import logging

class AbilityEndpoints:
    def __init__(self, db):
        self.collection = db['Abilities']
        self.abilityModel = AbilityModel(db)
        self.abilityStatistics = []
    
    def get_ability_by_id(self, abilityId):
        ability = self.abilityModel.get_ability_by_id(abilityId)
        if ability:
            return Ability.from_dict(ability).to_dict()
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
            id = data.get('id')
            ability_statistics_data = data.get("abilityStatistics", [])

            ability_statistics_list = [
                AbilityStatistics(
                    level = stat_data.get("level"),
                    oppHP = stat_data.get("oppHP"),
                    attGainedWhenLoseHP = stat_data.get("attGainedWhenLoseHP"),
                    yourSideDef = stat_data.get("yourSideDef"),
                    deathDamage = stat_data.get("deathDamage"),
                    poison = stat_data.get("poison"),
                    chargedBoom = stat_data.get("chargedBoom"),
                    sacrifice = stat_data.get("sacrifice"),
                ) for stat_data in ability_statistics_data
            ]

            self.update_statistics(ability_statistics_list)

            ability = Ability(
                name = data.get("name"),
                description = data.get("description"),
                icon = data.get("icon"),
                visualEffect = data.get("visualEffect"),
                abilityStatistics = ability_statistics_list
            )

            if self.abilityModel.update_ability(id, ability):
                return {"message": "ability updated successfully"}, 200
            else:
                return {"message": "ability not found or update failed"}, 404

        except Exception as e:
            return {"message": f"Failed to update ability: {str(e)}"}, 500
        
    def update_statistics(self, new_stats):
        for new_stat in new_stats:
            level = new_stat.level
            existing_stat = next(
                (stat for stat in self.abilityStatistics if stat.level == level),
                None
            )

            if existing_stat:
                existing_stat.level = new_stat.level
                existing_stat.oppHP = new_stat.oppHP
                existing_stat.attGainedWhenLoseHP = new_stat.attGainedWhenLoseHP
                existing_stat.yourSideDef = new_stat.yourSideDef
                existing_stat.deathDamage = new_stat.deathDamage
                existing_stat.poison = new_stat.poison
                existing_stat.chargedBoom = new_stat.chargedBoom
                existing_stat.sacrifice = new_stat.sacrifice
            else:
                self.abilityStatistics.append(new_stat)

    def create_ability(self, data):
        if not data:
            return {"message": "No data provided in the request"}, 400

        try:
            ability_statistics_data = data.get("abilityStatistics", [])
            logging.debug(ability_statistics_data)
            ability_statistics_list = [
                AbilityStatistics(
                    level = stat_data.get("level"),
                    oppHP = stat_data.get("oppHP"),
                    attGainedWhenLoseHP = stat_data.get("attGainedWhenLoseHP"),
                    yourSideDef = stat_data.get("yourSideDef"),
                    deathDamage = stat_data.get("deathDamage"),
                    poison = stat_data.get("poison"),
                    chargedBoom = stat_data.get("chargedBoom"),
                    sacrifice = stat_data.get("sacrifice"),
                ) for stat_data in ability_statistics_data
            ]

            ability = Ability(
                name = data.get("name"),
                description = data.get("description"),
                icon = data.get("icon"),
                visualEffect = data.get("visualEffect"),
                abilityStatistics = ability_statistics_list
            )

            abilityId = self.abilityModel.create_ability(ability)
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
            abilities_with_levels = []
            abilitiesOneLevel = self.abilityModel.get_abilities_by_level(data)
            abilities_with_levels = [Ability.from_dict(ability).to_dict() for ability in abilitiesOneLevel]
            return abilities_with_levels

        except Exception as e:
            return {"message": f"Failed to retrieve abilities: {str(e)}"}, 500