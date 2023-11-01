//
//  CharactersOwned.swift
//  Abilities-Unchained-Card-Duels
//
//  Created by Jeremy Marchesani on 10/28/23.
//

import Foundation

class CharacterOwned {
    var characterId: Int
    var level: Int
    var currentXp: Int
    
    init(characterId: Int, level: Int, currentXp: Int) {
        self.characterId = characterId
        self.level = level
        self.currentXp = currentXp
    }
}
