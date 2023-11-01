//
//  ContentView.swift
//  Abilities-Unchained-Card-Duels
//
//  Created by Jeremy Marchesani on 10/18/23.
//

import SwiftUI

struct ContentView: View {
    
    var body: some View {
        ZStack {
            Image("background-plain").resizable().ignoresSafeArea()
            
            TabView {
                GameplayView().tabItem { Text("Gameplay") }
                ChooseCharacters().tabItem { Text("Choose Characters" )}
            }
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
