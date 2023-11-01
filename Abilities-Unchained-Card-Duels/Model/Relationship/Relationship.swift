//
//  Relationship.swift
//  Abilities-Unchained-Card-Duels
//
//  Created by Jeremy Marchesani on 10/28/23.
//

import Foundation

class Relationship {
    var id: Int
    var initiatingUserId: String
    var receivingUserId: String
    var relationshipStatus: RelationshipEnum
    
    init(id: Int, initiatingUserId: String, receivingUserId: String, relationshipStatus: RelationshipEnum) {
        self.id = id
        self.initiatingUserId = initiatingUserId
        self.receivingUserId = receivingUserId
        self.relationshipStatus = relationshipStatus
    }
}
