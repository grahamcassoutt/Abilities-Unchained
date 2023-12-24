//
//  ChargedBoom.swift
//  Abilities-Unchained-Card-Duels
//
//  Created by Jeremy Marchesani on 10/28/23.
//

import Foundation

class ChargedBoom: Decodable {
    var multiplier: Double
    var numRoundsBetweenBoom: Int
    
    init(multiplier: Double, numRoundsBetweenBoom: Int) {
        self.numRoundsBetweenBoom = numRoundsBetweenBoom
        self.multiplier = multiplier
    }
}
