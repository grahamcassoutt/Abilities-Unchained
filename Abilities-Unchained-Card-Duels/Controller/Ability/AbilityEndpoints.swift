//
//  AbilityEndpoints.swift
//  Abilities-Unchained-Card-Duels
//
//  Created by Jeremy Marchesani on 12/23/23.
//

import Foundation

class AbilityEndpoints {
    let BASE_URL = "http://127.0.0.1:7050/api/"
    
    var GET_MULTIPLE_ABILITIES_BY_LEVEL_URL: String {
        return BASE_URL + "abilities/levels"
    }

    func getMultipleAbilitiesByLevel(inputAbility: [SimplifiedAbility]) async throws -> Dictionary<String, Any> {
        let url = URL(string: GET_MULTIPLE_ABILITIES_BY_LEVEL_URL)!

        var request = URLRequest(url: url)
        request.httpMethod = "POST"

        do {
            let jsonData = try JSONEncoder().encode(inputAbility)
            
            request.httpBody = jsonData
            request.setValue("application/json", forHTTPHeaderField: "Content-Type")

            let (data, _) = try await URLSession.shared.data(for: request)
            
            let ability: [Ability] = try JSONDecoder().decode([Ability].self, from: data)
            let reducedAbility = ability[0].reducedAbility()
            return reducedAbility
        } catch {
            print("Error in getMultipleAbilitiesByLevel: \(error)")
            throw error
        }
    }

}

