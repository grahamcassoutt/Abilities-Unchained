//
//  CharactersOnBoard.swift
//  Abilities-Unchained-Card-Duels
//
//  Created by Jeremy Marchesani on 10/28/23.
//

import Foundation

class CharactersOnBoard {
    var characterId: Int
    var attack: Int
    var defense: Int
    
    init(characterId: Int, attack: Int, defense: Int) {
        self.characterId = characterId
        self.attack = attack
        self.defense = defense
    }
}
