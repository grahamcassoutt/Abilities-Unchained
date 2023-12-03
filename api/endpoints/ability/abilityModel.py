import logging
import pymongo
from bson.objectid import ObjectId

class AbilityModel:
    def __init__(self, db):
        self.collection = db['abilities']

    def create_ability(self, ability):
        ability_document = ability.to_dict()
        logging.debug(ability_document)
        result = self.collection.insert_one(ability_document)
        return str(result.inserted_id)

    def get_ability_by_id(self, abilityId):
        ability = self.collection.find_one({"_id": ObjectId(abilityId)})
        return ability

    def update_ability(self, abilityId, ability):
        ability_document = ability.to_dict_for_update()
        levels = [stat['level'] for stat in ability_document['abilityStatistics']]

        # Update other dynamic fields
        update_operations = {
            '$set': {key: value for key, value in ability_document.items() if key != 'abilityStatistics' and key != '_id'}
        }

        # Update abilityStatistics individually
        for stat in ability_document['abilityStatistics']:
            level = stat['level']
            for key, value in stat.items():
                if key != 'level':
                    self.update_ability_statistic(abilityId, level, key, value)

        logging.debug(f"Query Criteria: {{'_id': ObjectId('{abilityId}')}}")
        logging.debug(f"Update Operations: {update_operations}")

        result = self.collection.update_one(
            {"_id": ObjectId(abilityId)},
            update_operations
        )

        if result.modified_count > 0:
            logging.debug("Update successful")
        else:
            logging.error(f"Update failed: {result.raw_result}")

        return result.modified_count > 0

    def update_ability_statistic(self, abilityId, level, key, value):
        logging.debug(f"Updating abilityStatistic for level {level}, key: {key}, value: {value}")

        result = self.collection.update_one(
            {"_id": ObjectId(abilityId), "abilityStatistics.level": level},
            {"$set": {f"abilityStatistics.$.{key}": value}}
        )

        if result.modified_count > 0:
            logging.debug("Update successful")
        else:
            logging.error(f"Update failed: {result.raw_result}")

        return result.modified_count > 0



    def delete_ability(self, abilityId):
        result = self.collection.delete_one({"_id": ObjectId(abilityId)})
        return result.deleted_count > 0
    
    def get_all_abilities(self):
        return list(self.collection.find())
    
    def get_characters_by_level(self, data):
        for req in data:
            req['abilityId'] = ObjectId(req['abilityId'])

        return self.collection.aggregate([
            {
                '$match': {'_id': {'$in': [req['abilityId'] for req in data]}}
            },
            {
                '$project': {
                    '_id': 1,
                    'name': 1,
                    'description': 1,
                    'icon': 1,
                    'visualEffect': 1,
                    'abilityStatistics': {
                        '$filter': {
                            'input': '$abilityStatistics',
                            'as': 'stat',
                            'cond': {'$eq': ['$$stat.level', {'$arrayElemAt': [{'$map': {'input': data, 'as': 'd', 'in': '$$d.level'}}, {'$indexOfArray': [{'$map': {'input': data, 'as': 'd', 'in': '$$d.abilityId'}}, '$_id']}]}]}
                        }
                    }
                }
            }
        ])
