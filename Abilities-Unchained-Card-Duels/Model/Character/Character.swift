//
//  Character.swift
//  Abilities-Unchained-Card-Duels
//
//  Created by Jeremy Marchesani on 10/27/23.
//

import Foundation

class Character: Identifiable, Decodable {
    var _id: String
    var name: String
    var description: String
    var backOfCardDescription: String
    var photoUrl: String
    var unlockedAt: Int
    var abilityId: String?
    var characterStatistics: [CharacterStatistics]

    init(_id: String, name: String, description: String, backOfCardDescription: String, photoUrl: String, unlockedAt: Int, abilityId: String? = nil, characterStatistics: [CharacterStatistics]) {
        self._id = _id
        self.name = name
        self.description = description
        self.backOfCardDescription = backOfCardDescription
        self.photoUrl = photoUrl
        self.unlockedAt = unlockedAt
        self.abilityId = abilityId
        self.characterStatistics = characterStatistics
    }
    
    func to_json() {
        
    }
}
