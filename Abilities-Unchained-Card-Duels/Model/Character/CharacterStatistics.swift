//
//  CharacterStatistics.swift
//  Abilities-Unchained-Card-Duels
//
//  Created by Jeremy Marchesani on 10/28/23.
//

import Foundation

class CharacterStatistics {
    var level: Int
    var health: Int
    var attack: Int
    var xpToUpgrade: Int
    var goldToUpgrade: Int
    
    init(level: Int, health: Int, attack: Int, xpToUpgrade: Int, goldToUpgrade: Int) {
        self.level = level
        self.health = health
        self.attack = attack
        self.xpToUpgrade = xpToUpgrade
        self.goldToUpgrade = goldToUpgrade
    }
}
