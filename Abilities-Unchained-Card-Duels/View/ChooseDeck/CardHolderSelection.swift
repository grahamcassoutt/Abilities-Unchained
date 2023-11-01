//
//  CardHolderSelection.swift
//  Abilities-Unchained-Card-Duels
//
//  Created by Jeremy Marchesani on 10/30/23.
//

import SwiftUI

struct CardHolderSelection: View {
    
    var hasAbility: Bool
    var character: Character?
    @State private var isPresented = false
    
    init(hasAbility: Bool, character: Character? = nil) {
        self.hasAbility = hasAbility
        self.character = character
    }
    
    var body: some View {
        
        VStack {
            EmptyCardHolder(character: character)
            Button(action: {
                isPresented.toggle()
            }) {
                Text("Choose").foregroundColor(Color.black)
            }
            .sheet(isPresented: $isPresented) {
                OwnedCharacters(charactersOwned: [], hasAbility: hasAbility)
            }
        }
    }
}

struct CardHolderSelection_Previews: PreviewProvider {
    static var previews: some View {
        CardHolderSelection(hasAbility: true)
    }
}
