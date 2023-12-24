//
//  AbilityOwned.swift
//  Abilities-Unchained-Card-Duels
//
//  Created by Jeremy Marchesani on 12/23/23.
//

import Foundation

class AbilityOwned {
    var abilityId: String
    var level: Int
    var currentXp: Int
    
    init(abilityId: String, level: Int, currentXp: Int) {
        self.abilityId = abilityId
        self.level = level
        self.currentXp = currentXp
    }
}

struct SimplifiedAbility: Encodable {
    var abilityId: String
    var level: Int
}
