//
//  Sacrifice.swift
//  Abilities-Unchained-Card-Duels
//
//  Created by Jeremy Marchesani on 10/28/23.
//

import Foundation

class Sacrifice: Decodable {
    var damageToCharacters: Int?
    var damageToHP: Int?
    
    init(damageToCharacters: Int? = nil, damageToHP: Int? = nil) {
        self.damageToCharacters = damageToCharacters
        self.damageToHP = damageToHP
    }
}
