//
//  Poison.swift
//  Abilities-Unchained-Card-Duels
//
//  Created by Jeremy Marchesani on 10/28/23.
//

import Foundation

class Poison: Decodable {
    var numberOfTurns: Int
    var damage: Int
    var reusable: Bool
    
    init(numberOfTurns: Int, damage: Int, reusable: Bool) {
        self.numberOfTurns = numberOfTurns
        self.damage = damage
        self.reusable = reusable
    }
}
