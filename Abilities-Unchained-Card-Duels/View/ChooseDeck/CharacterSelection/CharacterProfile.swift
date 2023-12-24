//
//  CharacterProfile.swift
//  Abilities-Unchained-Card-Duels
//
//  Created by Jeremy Marchesani on 10/28/23.
//

import SwiftUI

struct CharacterProfile: View {
    var character: Character
    var simplifiedAbility: SimplifiedAbility?
    let callback: () -> Void
    var hasAbility: Bool
    @State private var abilityStats: Dictionary<String, Any>?
    
    var width: CGFloat
    var height: CGFloat
    
    @State private var selectedTab = "Attributes"

    init(character: Character, simplifiedAbility: SimplifiedAbility?, hasAbility: Bool, callback: @escaping () -> Void) {
//    init(character: Character) {
        self.character = character
        self.simplifiedAbility = simplifiedAbility
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
            
            Text(character.name)
            
            Image(character.photoUrl)
                .resizable()
                .aspectRatio(contentMode: .fit)
                .frame(width: width, height: height / 3)
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
                DescriptionAndAbilityStats(abilityStats: abilityStats!)
                    .offset(y: height / 4)
            }
        }
        .onAppear {
            if (hasAbility) {
                fetchAbility();
            }
        }
        .frame(maxWidth: .infinity, maxHeight: .infinity)
    }
    
    private func fetchAbility() {
        Task {
            do {
                let endpoints = AbilityEndpoints()
                abilityStats = try await endpoints.getMultipleAbilitiesByLevel(
                    inputAbility: [simplifiedAbility!]
                )
            } catch {
                print("Error fetching characters: \(error.localizedDescription)")
            }
        }
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
            Statistics(characterStats: character.characterStatistics.first)
        }
    }
}

struct DescriptionAndAbilityStats: View {
    var abilityStats: Dictionary<String, Any>

    init(abilityStats: Dictionary<String, Any>) {
        self.abilityStats = abilityStats
    }

    var body: some View {
        VStack {
            if let name = abilityStats["name"] as? String {
                Text(name).padding(20)
            }

            if let description = abilityStats["description"] as? String {
                Text(description).padding(20)
            }
            AbilityStats(abilityStats: abilityStats)
        }
    }
}

struct Statistics: View {
    var characterStats: CharacterStatistics?
    
    init(characterStats: CharacterStatistics?) {
        self.characterStats = characterStats
    }
    
    var body: some View {
        VStack {
            HStack {
                Text("Level:")
                Text(String(characterStats!.level))
            }
            HStack {
                Text("Health:")
                Text(String(characterStats!.health))
            }
            HStack {
                Text("Attack:")
                Text(String(characterStats!.attack))
            }
        }
    }
}

struct AbilityStats: View {
    var abilityStats: Dictionary<String, Any>

    init(abilityStats: Dictionary<String, Any>) {
        self.abilityStats = abilityStats
        print(abilityStats)
    }

    var body: some View {
        VStack {
            if let level = abilityStats["level"] as? Int {
                HStack {
                    Text("Level: ")
                    Text(String(level)).padding(20)
                }
            }
            if let oppHP = abilityStats["oppHP"] as? Int {
                HStack {
                    Text("Opponent HP: ")
                    Text(String(oppHP)).padding(20)
                }
            }
            if let attGatinedWhenLoseHP = abilityStats["attGatinedWhenLoseHP"] as? Int {
                HStack {
                    Text("Attack Gained: ")
                    Text(String(attGatinedWhenLoseHP)).padding(20)
                }
            }
            if let yourSideDef = abilityStats["yourSideDef"] as? Int {
                HStack {
                    Text("Your Side Def: ")
                    Text(String(yourSideDef)).padding(20)
                }
            }
            if let deathDamage = abilityStats["deathDamage"] as? DeathDamage {
                HStack {
                    Text("Death Damage: ")
                    if let characters = deathDamage.characters {
                        Text(String(characters))
                        Text(" to characters")
                    }
                    if let hitpoints = deathDamage.hitPoints {
                        Text(String(hitpoints))
                        Text(" to enemy hitpoints")
                    }
                }
            }
            if let poison = abilityStats["poison"] as? Poison {
                HStack {
                    Text("Poison: ")
                    Text(String(poison.damage) + " for ")
                    Text(String(poison.numberOfTurns) + " turns")
                }
            }
            if let chargedBoom = abilityStats["chargedBoom"] as? ChargedBoom {
                HStack {
                    Text("Charged Boom: ")
                    Text(String(chargedBoom.multiplier) + "x every ")
                    Text(String(chargedBoom.numRoundsBetweenBoom) + " turns")
                }
            }
            if let sacrifice = abilityStats["sacrifice"] as? Sacrifice {
                HStack {
                    Text("Sacrifice: ")
                    if let damageToCharacters = sacrifice.damageToCharacters {
                        Text(String(damageToCharacters))
                        Text(" to characters")
                    }
                    if let damageToHP = sacrifice.damageToHP {
                        Text(String(damageToHP))
                        Text(" to enemy hitpoints")
                    }
                }
            }
        }
    }
}
