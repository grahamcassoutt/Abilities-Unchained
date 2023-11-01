//
//  ChooseCharacters.swift
//  Abilities-Unchained-Card-Duels
//
//  Created by Jeremy Marchesani on 10/30/23.
//

import SwiftUI

struct ChooseCharacters: View {
    
    var body: some View {
        ZStack {
            Image("background-plain").resizable().ignoresSafeArea()
            
            VStack {
                Spacer()
                Text("Normal Cards").font(.system(size: 30))
                HStack {
                    Spacer()
                    CardHolderSelection(hasAbility: false, character: nil)
                    Spacer()
                    CardHolderSelection(hasAbility: false, character: nil)
                    Spacer()
                    CardHolderSelection(hasAbility: false, character: nil)
                    Spacer()
                }
                Spacer()
                Text("Ability Cards").font(.system(size: 30))
                HStack {
                    Spacer()
                    CardHolderSelection(hasAbility: true, character: Character(name: "asdf", description: "asdf", backOfCardDescription: "back", photoUrl: "card11", unlockedAt: 2, characterStatistics: []))
                    Spacer()
                    CardHolderSelection(hasAbility: true, character: nil)
                    Spacer()
                    CardHolderSelection(hasAbility: true, character: nil)
                    Spacer()
                }
                Spacer()
            }.background(Color.clear)
        }
    }
}

struct ChooseCharacters_Previews: PreviewProvider {
    static var previews: some View {
        ChooseCharacters()
    }
}
