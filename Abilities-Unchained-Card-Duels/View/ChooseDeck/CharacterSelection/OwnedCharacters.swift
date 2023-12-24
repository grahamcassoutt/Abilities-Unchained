//
//  OwnedCharacters.swift
//  Abilities-Unchained-Card-Duels
//
//  Created by Jeremy Marchesani on 10/28/23.
//

import SwiftUI

struct OwnedCharacters: View {
    
    private var userCharacters: [CharacterOwned] = []
    @State private var charactersWithAbility: [CharacterAndAbility] = []
    @State private var charactersWithoutAbility: [Character] = []
    @State private var selectedCharacterWithAbility: CharacterAndAbility? = nil
    @State private var selectedCharacterWithoutAbility: Character? = nil
    @State private var isCharacterClicked: Bool = false
    private var hasAbility: Bool
    
    init(charactersOwned: [CharacterOwned], hasAbility: Bool) {
        self.userCharacters = charactersOwned
        self.hasAbility = hasAbility
    }
    
    var body: some View {
        ZStack {
            Image("background-plain").resizable().ignoresSafeArea()
            if !charactersWithAbility.isEmpty {
                ScrollView {
                    LazyVGrid(columns: [GridItem](repeating: GridItem(.flexible(), spacing: 16), count: 3), spacing: 16) {
                        ForEach(charactersWithAbility) { item in
                                Button(action: {
                                    selectedCharacterWithAbility = item
                                }) {
                                    Image(item.character.photoUrl)
                                        .resizable()
                                        .frame(width: UIScreen.main.bounds.size.width / 4, height: UIScreen.main.bounds.size.height / 5)
                                }
                            }
                    }
                    .padding(16)
                }
            } else {
                ScrollView {
                    LazyVGrid(columns: [GridItem](repeating: GridItem(.flexible(), spacing: 16), count: 3), spacing: 16) {
                            ForEach(charactersWithoutAbility) { item in
                                Button(action: {
                                    selectedCharacterWithoutAbility = item
                                }) {
                                    Image(item.photoUrl)
                                        .resizable()
                                        .frame(width: UIScreen.main.bounds.size.width / 4, height: UIScreen.main.bounds.size.height / 5)
                                }
                            }
                    }
                    .padding(16)
                }
            }
            
            if selectedCharacterWithAbility != nil {
                CharacterProfile(character: selectedCharacterWithAbility!.character, simplifiedAbility: selectedCharacterWithAbility?.ability, hasAbility: true, callback: {
                        selectedCharacterWithAbility = nil
                })
            }
            if selectedCharacterWithoutAbility != nil {
                CharacterProfile(character: selectedCharacterWithoutAbility!, simplifiedAbility: nil, hasAbility: false, callback: {
                        selectedCharacterWithoutAbility = nil
                })
            }
        }
        .onAppear {
            fetchCharacters()
        }
    }
    
    private func fetchCharacters() {
        Task {
            do {
                let endpoints = CharacterEndpoints()
                charactersWithoutAbility = []
                charactersWithAbility = []
                if (hasAbility) {
                    charactersWithAbility = try await endpoints.getMultipleCharactersByLevelWithAbility(
                        user: currentUser
                    )
                } else {
                    charactersWithoutAbility = try await endpoints.getMultipleCharactersByLevelWithoutAbility(
                        user: currentUser
                    )
                }
            } catch {
                print("Error fetching characters: \(error.localizedDescription)")
            }
        }
    }
}

//struct OwnedCharacters_Previews: PreviewProvider {
//    static var previews: some View {
//        ZStack {
//            Image("background-plain").resizable().ignoresSafeArea()
//
//            OwnedCharacters(charactersOwned: [
//                Character(_id: "1", name: "asdf", description: "asdf", backOfCardDescription: "back", photoUrl: "card11", unlockedAt: 1, characterStatistics: [CharacterStatistics(level: 1, health: 2, attack: 3, xpToUpgrade: 4, goldToUpgrade: 5)]),
//                Character(_id: "2", name: "asdf", description: "asdf", backOfCardDescription: "back", photoUrl: "card11", unlockedAt: 1, characterStatistics: [CharacterStatistics(level: 1, health: 2, attack: 3, xpToUpgrade: 4, goldToUpgrade: 5)]),
//                Character(_id: "3", name: "asdf", description: "asdf", backOfCardDescription: "back", photoUrl: "card11", unlockedAt: 1, characterStatistics: [CharacterStatistics(level: 1, health: 2, attack: 3, xpToUpgrade: 4, goldToUpgrade: 5)]
//                )],
//                hasAbility: true
//            )
//        }
//    }
//}
