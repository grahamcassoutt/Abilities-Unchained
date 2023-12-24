//
//  DefineUser.swift
//  Abilities-Unchained-Card-Duels
//
//  Created by Jeremy Marchesani on 12/23/23.
//

import Foundation

let currentUser: User = User(username: "asdf", email: "asdf", displayName: "asdf", isActive: true, level: 1, xp: 0, hitpoints: 2, trophies: 0, gold: 0, wins: 0, charactersOwned: [
    CharacterOwned(characterId: "65779278880edd5c74eec75e", level: 1, currentXp: 0, abilityStats: AbilityOwned(abilityId: "6587bed3c0fe2d70d1cfcc1e", level: 1, currentXp: 0)),
    CharacterOwned(characterId: "65779352880edd5c74eec75f", level: 1, currentXp: 0, abilityStats: AbilityOwned(abilityId: "6587c0afa682741cbf4f1351", level: 1, currentXp: 0)),
    CharacterOwned(characterId: "65779684880edd5c74eec761", level: 1, currentXp: 0, abilityStats: nil),
    CharacterOwned(characterId: "657793fd880edd5c74eec760", level: 1, currentXp: 0, abilityStats: nil),
    CharacterOwned(characterId: "65779b30880edd5c74eec764", level: 1, currentXp: 0, abilityStats: nil),
    CharacterOwned(characterId: "65779ba5880edd5c74eec765", level: 1, currentXp: 0, abilityStats: AbilityOwned(abilityId: "6587c0fda682741cbf4f1352", level: 1, currentXp: 0))],
                      abilityCardsSlected: [],
                         nonAbilityCardsSlected: [],
                         chests: UserChests(maxCount: 5, currCount: 0, chests: []))
