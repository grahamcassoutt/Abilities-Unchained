//
//  ChargedBoom.swift
//  Abilities-Unchained-Card-Duels
//
//  Created by Jeremy Marchesani on 10/28/23.
//

import Foundation

class ChargedBoom {
    var numRoundsBetweenBoom: Int
    var multiplier: Int
    
    init(numRoundsBetweenBoom: Int, multiplier: Int) {
        self.numRoundsBetweenBoom = numRoundsBetweenBoom
        self.multiplier = multiplier
    }
}
