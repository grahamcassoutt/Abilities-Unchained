//
//  CardsChosen.swift
//  Abilities-Unchained-Card-Duels
//
//  Created by Jeremy Marchesani on 10/28/23.
//

import Foundation

class CardsChosen {
    var characterId: Int
    var level: Int
    var isAlive: Bool
    
    init(characterId: Int, level: Int, isAlive: Bool) {
        self.characterId = characterId
        self.level = level
        self.isAlive = isAlive
    }
}
