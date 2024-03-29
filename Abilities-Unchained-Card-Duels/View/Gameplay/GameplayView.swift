//
//  GameplayView.swift
//  Abilities-Unchained-Card-Duels
//
//  Created by Jeremy Marchesani on 10/27/23.
//

import SwiftUI

struct GameplayView: View {
    
    //@State allows variable to be changed
    @State var player1Score: Int = 50
    @State var player2Score: Int = 50
    
    var body: some View {
        ZStack {
            Image("background-plain").resizable().ignoresSafeArea()
            
            VStack {
                Spacer()
                
                VStack {
                    Text("Player 2")
                        .font(.largeTitle)
                        .accessibilityLabel("Player2 Name")
                    
                    HStack {
                        Text("Health:")
                            .font(.title3)
                        Text(String(player2Score))
                            .font(.title3)
                    }
                }
                
                Spacer()
                EmptyCardHolderSet(
                    character1: Character(_id: "1", name: "asdf", description: "asdf", backOfCardDescription: "back", photoUrl: "card11", unlockedAt: 1, characterStatistics: [CharacterStatistics(level: 1, health: 2, attack: 3, xpToUpgrade: 4, goldToUpgrade: 5)]),
                    character2: Character(_id: "2", name: "asdf", description: "asdf", backOfCardDescription: "back", photoUrl: "card3", unlockedAt: 1, characterStatistics: [CharacterStatistics(level: 1, health: 2, attack: 3, xpToUpgrade: 4, goldToUpgrade: 5)]),
                    character3: nil
                )
                Spacer()
                EmptyCardHolderSet(
                    character1: Character(_id: "3", name: "asdf", description: "asdf", backOfCardDescription: "back", photoUrl: "card9", unlockedAt: 1, characterStatistics: [CharacterStatistics(level: 1, health: 2, attack: 3, xpToUpgrade: 4, goldToUpgrade: 5)]),
                    character2: Character(_id: "4", name: "asdf", description: "asdf", backOfCardDescription: "back", photoUrl: "card8", unlockedAt: 1, characterStatistics: [CharacterStatistics(level: 1, health: 2, attack: 3, xpToUpgrade: 4, goldToUpgrade: 5)]),
                    character3: Character(_id: "5", name: "asdf", description: "asdf", backOfCardDescription: "back", photoUrl: "card14", unlockedAt: 1, characterStatistics: [CharacterStatistics(level: 1, health: 2, attack: 3, xpToUpgrade: 4, goldToUpgrade: 5)])
                )
                Spacer()
                
                VStack {
                    HStack {
                        Text("Health:")
                            .font(.title3)
                        Text(String(player1Score))
                            .font(.title3)
                    }
                    
                    Text("Player 1")
                        .font(.largeTitle)
                        .accessibilityLabel("Player1 Name")
                }
                Spacer()
            }
        }
    }
}

struct GameplayView_Previews: PreviewProvider {
    static var previews: some View {
        GameplayView()
    }
}
