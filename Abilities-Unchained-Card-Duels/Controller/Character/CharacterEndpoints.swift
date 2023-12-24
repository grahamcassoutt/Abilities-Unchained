import Foundation

class CharacterEndpoints {
    let BASE_URL = "http://127.0.0.1:7050/api/"
    
    var GET_MULTIPLE_CHARACTERS_BY_LEVEL_URL: String {
        return BASE_URL + "characters/levels"
    }

    func getMultipleCharactersByLevelWithAbility(user: User) async throws -> [CharacterAndAbility] {
        var url = URL(string: GET_MULTIPLE_CHARACTERS_BY_LEVEL_URL)!
        var urlComponents = URLComponents(url: url, resolvingAgainstBaseURL: true)
        urlComponents?.path += "/true"
        if let updatedURL = urlComponents?.url {
            url = updatedURL
        }
        
        var request = URLRequest(url: url)
        request.httpMethod = "POST"
        
        var simplifiedCharacters: [SimplifiedCharacter] = []
        var simplifiedAbilities: [SimplifiedAbility] = []
        
        for characterOwned in user.charactersOwned {
            let simplifiedCharacter = SimplifiedCharacter(characterId: characterOwned.characterId, level: characterOwned.level)
            simplifiedCharacters.append(simplifiedCharacter)

            if let abilityOwned = characterOwned.abilityStats {
                let simplifiedAbility = SimplifiedAbility(abilityId: abilityOwned.abilityId, level: abilityOwned.level)
                simplifiedAbilities.append(simplifiedAbility)
            }
        }
        
        do {
            let jsonData = try JSONEncoder().encode(simplifiedCharacters)
            
            request.httpBody = jsonData
            request.setValue("application/json", forHTTPHeaderField: "Content-Type")

            let (data, _) = try await URLSession.shared.data(for: request)
            
            let characters: [Character] = try JSONDecoder().decode([Character].self, from: data)
            
            var characterAndAbilities: [CharacterAndAbility] = []

            for character in characters {
                if let characterAbilityId = character.abilityId {
                    if let matchingAbility = simplifiedAbilities.first(where: { $0.abilityId == characterAbilityId }) {
                        characterAndAbilities.append(CharacterAndAbility(character: character, ability: matchingAbility))
                    }
                }
            }
            return characterAndAbilities
        } catch {
            print("Error in getMultipleCharactersByLevel: \(error)")
            throw error
        }
    }
    
    func getMultipleCharactersByLevelWithoutAbility(user: User) async throws -> [Character] {
        var url = URL(string: GET_MULTIPLE_CHARACTERS_BY_LEVEL_URL)!
        var urlComponents = URLComponents(url: url, resolvingAgainstBaseURL: true)
        urlComponents?.path += "/false"
        if let updatedURL = urlComponents?.url {
            url = updatedURL
        }
        
        var request = URLRequest(url: url)
        request.httpMethod = "POST"
        
        let simplifiedCharacters: [SimplifiedCharacter] = user.charactersOwned.map {
            SimplifiedCharacter(characterId: $0.characterId, level: $0.level)
        }
        
        do {
            let jsonData = try JSONEncoder().encode(simplifiedCharacters)
            
            request.httpBody = jsonData
            request.setValue("application/json", forHTTPHeaderField: "Content-Type")

            let (data, _) = try await URLSession.shared.data(for: request)
            
            let characters = try JSONDecoder().decode([Character].self, from: data)
            return characters
        } catch {
            print("Error in getMultipleCharactersByLevel: \(error)")
            throw error
        }
    }

}
