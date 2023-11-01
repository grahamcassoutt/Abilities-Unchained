//
//  UserChest.swift
//  Abilities-Unchained-Card-Duels
//
//  Created by Jeremy Marchesani on 10/28/23.
//

import Foundation

class UserChest {
    var chestObject: Int
    var timeLeft: Timer
    var isActive: Bool
    
    init(chestObject: Int, timeLeft: Timer, isActive: Bool) {
        self.chestObject = chestObject
        self.timeLeft = timeLeft
        self.isActive = isActive
    }
}
