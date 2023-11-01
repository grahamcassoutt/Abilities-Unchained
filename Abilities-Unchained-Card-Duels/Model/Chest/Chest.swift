//
//  Chest.swift
//  Abilities-Unchained-Card-Duels
//
//  Created by Jeremy Marchesani on 10/28/23.
//

import Foundation

class Chest {
    var id: Int
    var rarity: String
    var xpAmount: Int
    var numDiffCards: Int
    var gold: Int
    var timeToOpen: Timer
    
    init(id: Int, rarity: String, xpAmount: Int, numDiffCards: Int, gold: Int, timeToOpen: Timer) {
        self.id = id
        self.rarity = rarity
        self.xpAmount = xpAmount
        self.numDiffCards = numDiffCards
        self.gold = gold
        self.timeToOpen = timeToOpen
    }
}
