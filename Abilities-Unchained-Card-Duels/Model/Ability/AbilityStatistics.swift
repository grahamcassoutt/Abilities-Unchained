//
//  AbilityStatistics.swift
//  Abilities-Unchained-Card-Duels
//
//  Created by Jeremy Marchesani on 10/28/23.
//

import Foundation

class AbilityStatistics: Decodable {
    var level: Int
    var oppHP: Int?
    var attGainedWhenLoseHP: Int?
    var yourSideDef: Int?
    var deathDamage: DeathDamage?
    var poison: Poison?
    var chargedBoom: ChargedBoom?
    var sacrifice: Sacrifice?
    
    init(level: Int, oppHP: Int? = nil, attGainedWhenLoseHP: Int? = nil, yourSideDef: Int? = nil, deathDamage: DeathDamage? = nil, poison: Poison? = nil, chargedBoom: ChargedBoom? = nil, sacrifice: Sacrifice? = nil) {
        self.level = level
        self.oppHP = oppHP
        self.attGainedWhenLoseHP = attGainedWhenLoseHP
        self.yourSideDef = yourSideDef
        self.deathDamage = deathDamage
        self.poison = poison
        self.chargedBoom = chargedBoom
        self.sacrifice = sacrifice
    }
    
    func getRelaventStats() -> Dictionary<String, Any> {
        var statsDictionary = Dictionary<String, Any>()
        
        statsDictionary["level"] = level
        
        if self.oppHP != 0 {
            statsDictionary["oppHP"] = oppHP!
        }
        if self.attGainedWhenLoseHP != 0 {
            statsDictionary["attGatinedWhenLoseHP"] = attGainedWhenLoseHP!
        }
        if self.yourSideDef != 0 {
            statsDictionary["yourSideDef"] = yourSideDef!
        }
        if self.deathDamage != nil {
            statsDictionary["deathDamage"] = deathDamage!
        }
        if self.poison != nil {
            statsDictionary["poison"] = poison!
        }
        if self.chargedBoom != nil {
            statsDictionary["chargedBoom"] = chargedBoom!
        }
        if self.sacrifice != nil {
            statsDictionary["sacrifice"] = sacrifice!
        }
        return statsDictionary
    }
}
