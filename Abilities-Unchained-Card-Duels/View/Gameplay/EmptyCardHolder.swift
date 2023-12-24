//
//  EmptyCardHolder.swift
//  Abilities-Unchained-Card-Duels
//
//  Created by Jeremy Marchesani on 10/26/23.
//

import SwiftUI

struct EmptyCardHolder: View {
    var character: Character?
    
    var width: CGFloat
    var height: CGFloat
    @State var currentCard: String

    init(character: Character? = nil) {
        self.character = character
        
        width = UIScreen.main.bounds.size.width / 4
        height = UIScreen.main.bounds.size.height / 5
        currentCard = character == nil ? "" : character!.photoUrl
    }

    var body: some View {
        ZStack {
            Rectangle()
                .frame(width: width, height: height)
                .foregroundColor(.clear)
                .overlay(
                    RoundedRectangle(cornerRadius: 0)
                        .stroke(Color.black, lineWidth: 2)
                )
            if (character != nil) {
                Button(action: {
                    if (currentCard == character!.photoUrl) {
                        currentCard = character!.backOfCardDescription
                    } else {
                        currentCard = character!.photoUrl
                    }
                    }) {
                        Image(currentCard)
                            .resizable()
                            .frame(width: width, height: height)
                    }
            }
        }
    }
}

struct EmptyCardHolder_Previews: PreviewProvider {
    static var previews: some View {
        EmptyCardHolder(character: Character(_id: "1", name: "asdf", description: "asdf", backOfCardDescription: "back", photoUrl: "card11", unlockedAt: 1, characterStatistics: [CharacterStatistics(level: 1, health: 2, attack: 3, xpToUpgrade: 4, goldToUpgrade: 5)]))
    }
}


