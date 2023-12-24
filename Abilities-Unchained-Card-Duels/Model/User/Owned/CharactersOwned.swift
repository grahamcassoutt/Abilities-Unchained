//
//  CharactersOwned.swift
//  Abilities-Unchained-Card-Duels
//
//  Created by Jeremy Marchesani on 10/28/23.
//

import Foundation

class CharacterOwned {
    var characterId: String
    var level: Int
    var currentXp: Int
    var abilityStats: AbilityOwned?
    
    init(characterId: String, level: Int, currentXp: Int, abilityStats: AbilityOwned?) {
        self.characterId = characterId
        self.level = level
        self.currentXp = currentXp
        self.abilityStats = abilityStats
    }
}

struct SimplifiedCharacter: Encodable {
    var characterId: String
    var level: Int
}
