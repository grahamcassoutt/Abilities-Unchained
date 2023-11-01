//
//  Character.swift
//  Abilities-Unchained-Card-Duels
//
//  Created by Jeremy Marchesani on 10/27/23.
//

import Foundation

class Character: Identifiable {
    var id: UUID = UUID()
    var name: String
    var description: String
    var backOfCardDescription: String
    var photoUrl: String
//    var type: Enum
    var unlockedAt: Int
    var AbilityId: Int?
    var characterStatistics: [CharacterStatistics]
    
    init(name: String, description: String, backOfCardDescription: String, photoUrl: String, unlockedAt: Int, AbilityId: Int? = nil, characterStatistics: [CharacterStatistics]) {
        self.name = name
        self.description = description
        self.backOfCardDescription = backOfCardDescription
        self.photoUrl = photoUrl
        self.unlockedAt = unlockedAt
        self.AbilityId = AbilityId
        self.characterStatistics = characterStatistics
    }
}
