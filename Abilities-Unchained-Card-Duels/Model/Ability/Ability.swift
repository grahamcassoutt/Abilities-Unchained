//
//  Ability.swift
//  Abilities-Unchained-Card-Duels
//
//  Created by Jeremy Marchesani on 10/28/23.
//

import Foundation

class Ability {
    var id: Int
    var name: String
    var description: String
    var icon: String
    var visualEffect: String
    var abilityStatistics: AbilityStatistics
    
    init(id: Int, name: String, description: String, icon: String, visualEffect: String, abilityStatistics: AbilityStatistics) {
        self.id = id
        self.name = name
        self.description = description
        self.icon = icon
        self.visualEffect = visualEffect
        self.abilityStatistics = abilityStatistics
    }
}
