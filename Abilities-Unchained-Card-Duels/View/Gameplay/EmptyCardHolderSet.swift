//
//  EmptyCardHolderSet.swift
//  Abilities-Unchained-Card-Duels
//
//  Created by Jeremy Marchesani on 10/27/23.
//

import SwiftUI

struct EmptyCardHolderSet: View {
    
    var character1: Character?
    var character2: Character?
    var character3: Character?
    
    init(character1: Character? = nil, character2: Character? = nil, character3: Character? = nil) {
        self.character1 = character1
        self.character2 = character2
        self.character3 = character3
    }
    
    var body: some View {
        HStack {
            Spacer()
            EmptyCardHolder(character: character1)
            Spacer()
            EmptyCardHolder(character: character2)
            Spacer()
            EmptyCardHolder(character: character3)
            Spacer()
        }
    }
}

struct EmptyCardHolderSet_Previews: PreviewProvider {
    static var previews: some View {
        EmptyCardHolderSet(
            character1: Character(name: "asdf", description: "asdf", backOfCardDescription: "back", photoUrl: "card11", unlockedAt: 1, characterStatistics: CharacterStatistics(level: 1, health: 2, attack: 3, xpToUpgrade: 4, goldToUpgrade: 5)),
            character2: Character(name: "asdf", description: "asdf", backOfCardDescription: "back", photoUrl: "card7", unlockedAt: 1, characterStatistics: CharacterStatistics(level: 1, health: 2, attack: 3, xpToUpgrade: 4, goldToUpgrade: 5)),
            character3: nil
        )
    }
}
