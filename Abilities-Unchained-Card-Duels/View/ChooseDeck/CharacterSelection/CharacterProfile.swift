//
//  CharacterProfile.swift
//  Abilities-Unchained-Card-Duels
//
//  Created by Jeremy Marchesani on 10/28/23.
//

import SwiftUI

struct CharacterProfile: View {
    var character: Character
    let callback: () -> Void
    var hasAbility: Bool
    
    var width: CGFloat
    var height: CGFloat
    
    @State private var selectedTab = "Attributes"

    init(character: Character, hasAbility: Bool, callback: @escaping () -> Void) {
//    init(character: Character) {
        self.character = character
        self.hasAbility = hasAbility
        self.callback = callback
        
        width = UIScreen.main.bounds.size.width / 1.5
        height = UIScreen.main.bounds.size.height / 1.5
    }
    
    var body: some View {
        
        ZStack {
            Image("background-plain").resizable()
            
            Rectangle()
                .frame(width: width, height: height)
                .foregroundColor(.clear)
                .overlay(
                    RoundedRectangle(cornerRadius: 0)
                        .stroke(Color.black, lineWidth: 2)
                )
                .background(Color.white)
            
            Button(action: {
                callback()
            }) {
                Image(systemName: "xmark.circle.fill")
                    .font(.title)
                    .foregroundColor(.red)
                    .background(Color.white)
                    .clipShape(Circle())
                    .padding(10)
            }
            .offset(x: -width / 2, y: -height / 2)
            
            Image(character.photoUrl)
                .resizable()
                .aspectRatio(contentMode: .fit)
                .frame(width: width, height: height / 3) // Adjust the padding here
                .offset(y: -((height / 3) - 10))
            
            HStack {
                Button(action: {
                    selectedTab = "Attributes"
                }) {
                    Text("Attributes")
                }
                .padding(10)
                .background(selectedTab == "Attributes" ? Color.blue : Color.gray)
                .foregroundColor(.white)
                
                if (hasAbility) {
                    Button(action: {
                        selectedTab = "Ability"
                    }) {
                        Text("Ability")
                    }
                    .padding(10)
                    .background(selectedTab == "Ability" ? Color.blue : Color.gray)
                    .foregroundColor(.white)
                }
            }
            
            if selectedTab == "Attributes" {
                DescriptionAndStats(character: character)
                    .offset(y: height / 4)
            } else if selectedTab == "Ability" {
                Text("Ability Tab Content")
                    .offset(y: height / 4)
            }
        }
        .frame(maxWidth: .infinity, maxHeight: .infinity)
    }
}

//struct CharacterProfile_Previews: PreviewProvider {
//    static var previews: some View {
//        CharacterProfile(character: Character(name: "asdf", description: "asdf", backOfCardDescription: "back", photoUrl: "card11", unlockedAt: 1, characterStatistics: CharacterStatistics(level: 1, health: 10, attack: 5, xpToUpgrade: 100, goldToUpgrade: 2000))
////                         callback:
//        )
//    }
//}

struct DescriptionAndStats: View {
    var character: Character
    
    init(character: Character) {
        self.character = character
    }
    
    var body: some View {
        VStack {
            Text(character.description)
                .padding(10)
            Statistics(characterStats: character.characterStatistics[0])
        }
    }
}

struct Statistics: View {
    var characterStats: CharacterStatistics
    
    init(characterStats: CharacterStatistics) {
        self.characterStats = characterStats
    }
    
    var body: some View {
        VStack {
            HStack {
                Text("Level:")
                Text(String(characterStats.level))
            }
            HStack {
                Text("Health:")
                Text(String(characterStats.health))
            }
            HStack {
                Text("Attack:")
                Text(String(characterStats.attack))
            }
        }
    }
}
