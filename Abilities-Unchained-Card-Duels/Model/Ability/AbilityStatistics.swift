//
//  AbilityStatistics.swift
//  Abilities-Unchained-Card-Duels
//
//  Created by Jeremy Marchesani on 10/28/23.
//

import Foundation

class AbilityStatistics {
    var level: Int
    var oppHP: Int
    var attGainedWhenLoseHP: Int
    var yourSideDef: Int
    var deathDamage: DeathDamage
    var poison: Poison?
    var chargedBoom: ChargedBoom?
    var sacrifice: Sacrifice?
    
    init(level: Int, oppHP: Int, attGainedWhenLoseHP: Int, yourSideDef: Int, deathDamage: DeathDamage, poison: Poison? = nil, chargedBoom: ChargedBoom? = nil, sacrifice: Sacrifice? = nil) {
        self.level = level
        self.oppHP = oppHP
        self.attGainedWhenLoseHP = attGainedWhenLoseHP
        self.yourSideDef = yourSideDef
        self.deathDamage = deathDamage
        self.poison = poison
        self.chargedBoom = chargedBoom
        self.sacrifice = sacrifice
    }
}
