#TicTacToe
#Geplante Features: Singleplayer vs Bot. / Online Multiplayer? / GUI?
#Ersteller: Tobias Dominik Weber aka. MisterNSA 
#Version: 0.7 Datum: 23.02.2020

import TicTacToe

def Menu():

    Menu_item = int(input("Do you want to play an new multiplayer game (1) or read through the rules (2)?"))

    if Menu_item == 1:
        TicTacToe.Multiplayer_Game()
    elif Menu_item == 2:
        TicTacToe.Rules()
        TicTacToe.Menu()
    else:
        Print("Please enter a valid Number and confirm with the Enter-Key")

Menu()

"""PROBLEM MIT player_move Zeile 19"""