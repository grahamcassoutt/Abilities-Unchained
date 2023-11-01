//
//  User.swift
//  Abilities-Unchained-Card-Duels
//
//  Created by Jeremy Marchesani on 10/28/23.
//

import Foundation

class User: Identifiable {
    var id: UUID
    var username: String
    var email: String
    var displayName: String
    var isActive: Bool
    var level: Int
    var xp: Int
    var hitpoints: Int
    var trophies: Int
    var gold: Int
    var wins: Int
    var charactersOwned: [CharacterOwned]
    var game: UserGame
    var chests: UserChests
    
    init(username: String, email: String, displayName: String, isActive: Bool, level: Int, xp: Int, hitpoints: Int, trophies: Int, gold: Int, wins: Int, charactersOwned: [CharacterOwned], game: UserGame, chests: UserChests) {
        self.id = UUID()
        self.username = username
        self.email = email
        self.displayName = displayName
        self.isActive = isActive
        self.level = level
        self.xp = xp
        self.hitpoints = hitpoints
        self.trophies = trophies
        self.gold = gold
        self.wins = wins
        self.charactersOwned = charactersOwned
        self.game = game
        self.chests = chests
    }
}
