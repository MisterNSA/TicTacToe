#TicTacToe
#Geplante Features: Singleplayer vs Bot. / Online Multiplayer? / GUI?
#Ersteller: Tobias Dominik Weber aka. MisterNSA 
#Version: 0.2 Datum: 21.02.2020

import TicTacToe

def Menu():
    
    Menu_item = int(input("Do you want to play an new game (1) or read through the rules (2)?"))

    if Menu_item == 1:
        game()
    elif Menu_item == 2:
        TicTacToe.Rules()
    else:
        Print("Please enter a valid Number and confirm with the Enter-Key")




    def game():
        
        board = [" "," "," "," "," "," "," "," "," "," "]
        Next_Turn == "Player1"

        while Win() != True: #Solange Sieg nicht bestätigt
            if Win() == "Draw":
                another_one = int(input("---Draw!---\nDo you want to play another game? Y/N"))
                if another_one == "Y" or "y":
                    game()
                else:
                    break
            
            if Next_Turn == "Player1"   #Wenn als nächstes Spieler 1 dran ist
                Player = "Player1"      #Momentaner Spieler
                TicTacToe.player_move(board, "X")   #Spieler 1 ist am Zug. Zeichen von Spieler 1 ist X
                Next_Turn = "Player2"   #Nächste Spieler, der dran ist
            else:
                Player = "Player2"      #Momentaner Spieler
                TicTacToe.player_move(board, "O")   #Spieler 2 ist am Zug. Zeichen von Spieler 1 ist 0
                Next_Turn = "Player1"   #Nächste Spieler, der dran ist
        else:
            print(Player + "Won!")
            another_one = int(input("Do you want to play another game? Y/N"))
            if another_one == "Y" or "y":
                game()
            else:
                break
Menu()









#if __name__ == '__main__':  #Wenn dies das Main-Programm ist 