//
//  CharacterStatistics.swift
//  Abilities-Unchained-Card-Duels
//
//  Created by Jeremy Marchesani on 10/28/23.
//

import Foundation

class CharacterStatistics: Decodable {
    var level: Int
    var health: Int
    var attack: Int
    var xpToUpgrade: Int
    var goldToUpgrade: Int
    
    init(level: Int, health: Int, attack: Int, xpToUpgrade: Int, goldToUpgrade: Int) {
        self.level = level
        self.health = health
        self.attack = attack
        self.xpToUpgrade = xpToUpgrade
        self.goldToUpgrade = goldToUpgrade
    }
    
//    static func toCharacterStatistics(from json: String) -> CharacterStatistics? {
//            guard let jsonData = json.data(using: .utf8) else {
//                print("Error converting JSON string to data.")
//                return nil
//            }
//
//            do {
//                let decoder = JSONDecoder()
//                let characterStatistics = try decoder.decode(CharacterStatistics.self, from: jsonData)
//                return characterStatistics
//            } catch {
//                print("Error decoding JSON: \(error.localizedDescription)")
//                return nil
//            }
//        }
}
