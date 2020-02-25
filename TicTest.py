#TicTacToe
#Geplante Features: Singleplayer vs Bot(Erledigt) / Online Multiplayer? / GUI?
#Ersteller: Tobias Dominik Weber aka. MisterNSA 
#Version: 1.0 Datum: 25.02.2020

import TicTacToe

def Menu():

    Menu_item = int(input("Do you want to play an new multiplayer game (1), play singleplayer (2) or read through the rules (3)?"))

    if Menu_item == 1:
        TicTacToe.Multiplayer_Game()
    elif Menu_item == 2:
        TicTacToe.Singleplayer_Game()
    elif Menu_item == 3:
        TicTacToe.Rules()
        Menu()
    else:
        print("Please enter a valid Number and confirm with the Enter-Key")
        Menu()

Menu()

