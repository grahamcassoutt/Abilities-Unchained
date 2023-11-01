//
//  UserChests.swift
//  Abilities-Unchained-Card-Duels
//
//  Created by Jeremy Marchesani on 10/28/23.
//

import Foundation

class UserChests {
    var maxCount: Int
    var currCount: Int
    var chests: [UserChests]
    
    init(maxCount: Int, currCount: Int, chests: [UserChests]) {
        self.maxCount = maxCount
        self.currCount = currCount
        self.chests = chests
    }
}
