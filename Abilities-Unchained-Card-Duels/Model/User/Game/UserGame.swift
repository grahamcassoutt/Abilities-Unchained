//
//  UserGame.swift
//  Abilities-Unchained-Card-Duels
//
//  Created by Jeremy Marchesani on 10/28/23.
//

import Foundation

class UserGame {
    var hitpoints: Int
    var cardsChosen: [CardsChosen]
    var charactersOnBoard: [CharactersOnBoard]
    
    init(hitpoints: Int, cardsChosen: [CardsChosen], charactersOnBoard: [CharactersOnBoard]) {
        self.hitpoints = hitpoints
        self.cardsChosen = cardsChosen
        self.charactersOnBoard = charactersOnBoard
    }
}
