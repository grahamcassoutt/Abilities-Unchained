//
//  Game.swift
//  Abilities-Unchained-Card-Duels
//
//  Created by Jeremy Marchesani on 10/28/23.
//

import Foundation

class Game {
    var id: Int
    var timestamp: Date
    var playerAId: String
    var playerBId: String
    var winner: String
    var playerACardsUsedIds: [Int]
    var playerBCardsUsedIds: [Int]
    
    init(id: Int, timestamp: Date, playerAId: String, playerBId: String, winner: String, playerACardsUsedIds: [Int], playerBCardsUsedIds: [Int]) {
        self.id = id
        self.timestamp = timestamp
        self.playerAId = playerAId
        self.playerBId = playerBId
        self.winner = winner
        self.playerACardsUsedIds = playerACardsUsedIds
        self.playerBCardsUsedIds = playerBCardsUsedIds
    }
}
