//
//  DeathDamage.swift
//  Abilities-Unchained-Card-Duels
//
//  Created by Jeremy Marchesani on 10/28/23.
//

import Foundation
 
class DeathDamage {
    var characters: Int?
    var hitPoints: Int?
    
    init(characters: Int? = nil, hitPoints: Int? = nil) {
        self.characters = characters
        self.hitPoints = hitPoints
    }
}
