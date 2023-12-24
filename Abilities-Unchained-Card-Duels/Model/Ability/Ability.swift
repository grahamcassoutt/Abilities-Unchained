//
//  Ability.swift
//  Abilities-Unchained-Card-Duels
//
//  Created by Jeremy Marchesani on 10/28/23.
//

import Foundation

class Ability: Identifiable, Decodable {
    var _id: String
    var name: String
    var description: String
    var icon: String
    var visualEffect: String
    var abilityStatistics: [AbilityStatistics]
    
    init(_id: String, name: String, description: String, icon: String, visualEffect: String, abilityStatistics: [AbilityStatistics]) {
        self._id = _id
        self.name = name
        self.description = description
        self.icon = icon
        self.visualEffect = visualEffect
        self.abilityStatistics = abilityStatistics
    }
    
    func reducedAbility() -> Dictionary<String, Any> {
        var reducedStats: Dictionary<String, Any> = self.abilityStatistics[0].getRelaventStats()
                
        reducedStats["name"] = self.name
        reducedStats["description"] = self.description
        reducedStats["icon"] = self.icon
        reducedStats["visualEffect"] = self.visualEffect
        return reducedStats
    }
}
