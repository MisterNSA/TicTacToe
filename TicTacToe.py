#Funktionsbibliothek für TicTacToe
#Ersteller: Tobias Dominik Weber aka. MisterNSA 
#Version: 0.7 Datum: 23.02.2020


#Zeigt das Feld an
def drawBoard(board):                                                    
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])


#Nimmt Input entgegen, prüft ob Zug möglich ist und führt diesen aus
def player_move(board, sign, Player):
    while True:
        """PROBLEM: WENN FIELD KEIN INT -> CRASH!!!"""
        field = int(input("On which field do you want to place a {} {}? 1-9: ".format(sign, Player)))  #Auswählen auf welchem Feld das Zeichen gesetzt werden soll
        if field < 1 or field > 9:      #Wenn Feld auserhalb der Reichweite
            print("Please Input a Number between 1 and 9 to choose your field. 1 for the top left and 9 for the bottom right.")
        elif board[field] != " ":       #Wenn schon ein Wert im Feld steht
            print("Theres already a {} in this Field. Please choose another one.".format(sign))
        else:
            break   
    board[field] = sign #In Liste board momentanes Feld mit Zeichen beschreiben
    drawBoard(board)


#Shows the rules of the game
def Rules():  
    print("The Goal of this Game is to be the first Player with three Symbols in a row.")
    print("Rows count horizontal, vertical and diagonal.")
    print("When the Game asks you to input a Number to choose a field and confirm with the Enter-Key. The fields are addressed with the following numbers:\n 1 | 2 | 3\n-----------\n 4 | 5 | 6\n-----------\n 7 | 8 | 9")

#Überprüft, ob Jemand das Spiel gewonnen hat (True), alle Felder belegt wurden ohne Sieger("Draw"), oder es noch Zugmöglichkeiten gibt(False). 
"""Erstmal alle Möglichkeiten durchzutesten / Später Neuronales Netz?"""
def Win(board, Turn_Count):
    if Turn_Count >= 5:  #Wenn Spieler 1 schon 3 mal dran war und somit die erste Chance hat zu gewinnen
        if board[7] == board[8] == board[9] != ' ': # across the bottom
            return True       
            pass
        elif board[4] == board[5] == board[6] != ' ': # across the middle
            return True
            pass
        elif board[1] == board[2] == board[3] != ' ': # across the top
            return True
            pass
        elif board[1] == board[4] == board[7] != ' ': # down the left side
            return True
            pass
        elif board[2] == board[5] == board[8] != ' ': # down the middle
            return True
            pass
        elif board[3] == board[6] == board[9] != ' ': # down the right side
            return True
            pass 
        elif board[7] == board[5] == board[3] != ' ': # diagonal
            return True
            pass
        elif board[1] == board[5] == board[9] != ' ': # diagonal
            return True
            pass 
        elif Turn_Count == 9:    #Wenn jedes Feld belegt ist
            return ("Draw")

    

#The Multiplayer Game
def Multiplayer_Game():
            board = [" "," "," "," "," "," "," "," "," "," "]
            Next_Turn = "Player 1"
            Turn_Count = 0

            while Win(board, Turn_Count) != True: #Solange Sieg nicht bestätigt
                if Win(board, Turn_Count) == "Draw":  #Solange kein Unentschieden
                    another_one = input("---Draw!---\nDo you want to play another game? Y/N ") #Abfragen, ob neues Spiel gestartet werden soll
                    if another_one == "Y" or another_one == "y":
                        Multiplayer_Game()
                    else:
                        break

                if Next_Turn == "Player 1":   #Wenn als nächstes Spieler 1 dran ist
                    Player  = "Player 1"      #Momentaner Spieler
                    player_move(board, "X", Player)   #Spieler 1 ist am Zug. Zeichen von Spieler 1 ist X
                    Next_Turn = "Player 2"   #Nächste Spieler, der dran ist
                    Turn_Count += 1         #Zug um 1 erhöhen
                else:
                    Player = "Player 2"      #Momentaner Spieler
                    player_move(board, "O", Player)   #Spieler 2 ist am Zug. Zeichen von Spieler 2 ist 0
                    Next_Turn = "Player 1"   #Nächste Spieler, der dran ist
                    Turn_Count += 1         #Zug um 1 erhöhen

            else:
                print(Player + " Won!")  #Ausgeben, wer gewonnen hat
                another_one = input("Do you want to play another game? Y/N ")  #Abfragen, ob neues Spiel gestartet werden soll
                if another_one == "Y" or another_one == "y":
                    Multiplayer_Game()
                else:
                    pass
