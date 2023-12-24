//
//  CharacterAndAbility.swift
//  Abilities-Unchained-Card-Duels
//
//  Created by Jeremy Marchesani on 12/23/23.
//

import Foundation

class CharacterAndAbility: Identifiable {
    var character: Character
    var ability: SimplifiedAbility
    
    init(character: Character, ability: SimplifiedAbility) {
        self.character = character
        self.ability = ability
    }
}
