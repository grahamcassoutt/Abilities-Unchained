//
//  OwnedCharacters.swift
//  Abilities-Unchained-Card-Duels
//
//  Created by Jeremy Marchesani on 10/28/23.
//

import SwiftUI

struct OwnedCharacters: View {
    
    var charactersOwned: [CharacterOwned]
    var hasAbility: Bool
    var characters: [Character]
    
    @State var selectedCharacter: Character? = nil
    @State var isCharacterClicked: Bool = false
    
    init(charactersOwned: [CharacterOwned], hasAbility: Bool) {
        self.charactersOwned = charactersOwned
        self.hasAbility = hasAbility
        characters = [
                      Character(name: "asdf", description: "asdf", backOfCardDescription: "back", photoUrl: "card11", unlockedAt: 2, characterStatistics: CharacterStatistics(level: 1, health: 100, attack: 5, xpToUpgrade: 100, goldToUpgrade: 2000)),
                      Character(name: "asdf", description: "asdf", backOfCardDescription: "back", photoUrl: "card14", unlockedAt: 2, characterStatistics: CharacterStatistics(level: 10, health: 10, attack: 5, xpToUpgrade: 100, goldToUpgrade: 2000)),
                      Character(name: "asdf", description: "asdf", backOfCardDescription: "back", photoUrl: "card9", unlockedAt: 2, characterStatistics: CharacterStatistics(level: 1, health: 10, attack: 50, xpToUpgrade: 100, goldToUpgrade: 2000)),
                      Character(name: "asdf", description: "asdf", backOfCardDescription: "back", photoUrl: "card2", unlockedAt: 2, characterStatistics: CharacterStatistics(level: 1, health: 101, attack: 5, xpToUpgrade: 100, goldToUpgrade: 2000)),
                      Character(name: "asdf", description: "asdf", backOfCardDescription: "back", photoUrl: "card11", unlockedAt: 2, characterStatistics: CharacterStatistics(level: 11, health: 10, attack: 5, xpToUpgrade: 100, goldToUpgrade: 2000)),
                      Character(name: "asdf", description: "asdf", backOfCardDescription: "back", photoUrl: "card14", unlockedAt: 2, characterStatistics: CharacterStatistics(level: 1, health: 10, attack: 51, xpToUpgrade: 100, goldToUpgrade: 2000)),
                      Character(name: "asdf", description: "asdf", backOfCardDescription: "back", photoUrl: "card9", unlockedAt: 2, characterStatistics: CharacterStatistics(level: 1, health: 102, attack: 5, xpToUpgrade: 100, goldToUpgrade: 2000)),
                      Character(name: "asdf", description: "asdf", backOfCardDescription: "back", photoUrl: "card11", unlockedAt: 2, characterStatistics: CharacterStatistics(level: 12, health: 10, attack: 5, xpToUpgrade: 100, goldToUpgrade: 2000)),
                      Character(name: "asdf", description: "asdf", backOfCardDescription: "back", photoUrl: "card14", unlockedAt: 2, characterStatistics: CharacterStatistics(level: 1, health: 10, attack: 52, xpToUpgrade: 100, goldToUpgrade: 2000)),
                      Character(name: "asdf", description: "asdf", backOfCardDescription: "back", photoUrl: "card9", unlockedAt: 2, characterStatistics: CharacterStatistics(level: 1, health: 103, attack: 5, xpToUpgrade: 100, goldToUpgrade: 2000)),
                      Character(name: "asdf", description: "asdf", backOfCardDescription: "back", photoUrl: "card2", unlockedAt: 2, characterStatistics: CharacterStatistics(level: 13, health: 10, attack: 5, xpToUpgrade: 100, goldToUpgrade: 2000)),
                      Character(name: "asdf", description: "asdf", backOfCardDescription: "back", photoUrl: "card11", unlockedAt: 2, characterStatistics: CharacterStatistics(level: 1, health: 10, attack: 53, xpToUpgrade: 100, goldToUpgrade: 2000)),
                      Character(name: "asdf", description: "asdf", backOfCardDescription: "back", photoUrl: "card14", unlockedAt: 2, characterStatistics: CharacterStatistics(level: 1, health: 104, attack: 5, xpToUpgrade: 100, goldToUpgrade: 2000)),
                      Character(name: "asdf", description: "asdf", backOfCardDescription: "back", photoUrl: "card9", unlockedAt: 2, characterStatistics: CharacterStatistics(level: 14, health: 10, attack: 5, xpToUpgrade: 100, goldToUpgrade: 2000))
        ]
    }
    
    var body: some View {
        ZStack {
            Image("background-plain").resizable().ignoresSafeArea()
            ScrollView {
                LazyVGrid(columns: [GridItem](repeating: GridItem(.flexible(), spacing: 16), count: 3), spacing: 16) {
                        ForEach(characters) { item in
                            Button(action: {
                                selectedCharacter = item
                            }) {
                                Image(item.photoUrl)
                                    .resizable()
                                    .frame(width: UIScreen.main.bounds.size.width / 4, height: UIScreen.main.bounds.size.height / 5)
                            }
                        }
                }
                .padding(16)
            }
            
            if (selectedCharacter != nil) {
                CharacterProfile(character: selectedCharacter!, hasAbility: hasAbility, callback: {
                        selectedCharacter = nil
                })
            }
        }
    }
}

struct OwnedCharacters_Previews: PreviewProvider {
    static var previews: some View {
        ZStack {
            Image("background-plain").resizable().ignoresSafeArea()
            
            OwnedCharacters(charactersOwned: [
                CharacterOwned(characterId: 1, level: 2, currentXp: 3),
                CharacterOwned(characterId: 2, level: 2, currentXp: 3),
                CharacterOwned(characterId: 3, level: 2, currentXp: 3)
                ],
                hasAbility: true
            )
        }
    }
}
