#Funktionsbibliothek für TicTacToe
#Ersteller: Tobias Dominik Weber aka. MisterNSA 
#Version: 0.9 Datum: 25.02.2020

import random

#Zeigt das Feld an
def drawBoard(board):                                                    
    print(" " + board[1] + " " + "|" + " " + board[2] + " " +  "|" + " " + board[3] + " ")
    print('---+---+---')
    print(" " + board[4] + " " + "|" + " " + board[5] + " " +  "|" + " " + board[6] + " ")
    print('---+---+---')
    print(" " + board[7] + " " + "|" + " " + board[8] + " " +  "|" + " " + board[9] + " \n")
            

#Shows the rules of the game
def Rules():  
    print("The Goal of this Game is to be the first Player with three Symbols in a row.")
    print("Rows count horizontal, vertical and diagonal.")
    print("When the Game asks you to input a Number to choose a field and confirm with the Enter-Key. The fields are addressed with the following numbers:\n")
    print(" " + "1" + " " + "|" + " " + "2" + " " +  "|" + " " + "3" + " ")
    print('---+---+---')
    print(" " + "4" + " " + "|" + " " + "5" + " " +  "|" + " " + "6" + " ")
    print('---+---+---')
    print(" " + "7" + " " + "|" + " " + "8" + " " +  "|" + " " + "9" + " \n")

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
            player_move(board, "X", Player, Turn_Count)   #Spieler 1 ist am Zug. Zeichen von Spieler 1 ist X
            Next_Turn = "Player 2"   #Nächste Spieler, der dran ist
            Turn_Count += 1         #Zug um 1 erhöhen
            drawBoard(board)
        else:
            Player = "Player 2"      #Momentaner Spieler
            player_move(board, "O", Player, Turn_Count)   #Spieler 2 ist am Zug. Zeichen von Spieler 2 ist 0
            Next_Turn = "Player 1"   #Nächste Spieler, der dran ist
            Turn_Count += 1         #Zug um 1 erhöhen
            drawBoard(board)
    else:
        print(Player + " Won!")  #Ausgeben, wer gewonnen hat
        another_one = input("Do you want to play another game? Y/N ")  #Abfragen, ob neues Spiel gestartet werden soll
        if another_one == "Y" or another_one == "y":
            Multiplayer_Game()
        else:
            pass


#Play against the Computer
def Singleplayer_Game():
    board = [" "," "," "," "," "," "," "," "," "," "]
    Turn_Count = 0

    plays_first = random.randint(1, 2) #Zufallsauswahl, ob spieler oder Computer zuerst dran ist / 1=Spieler 2=Computer
    if plays_first == 1:
        Next_Turn = "Player 1"
        print("Player 1 plays first!")
    else:
        Next_Turn = "Computer"
        print("Computer plays first!")

    while Win(board, Turn_Count) != True: #Solange Sieg nicht bestätigt
        if Win(board, Turn_Count) == "Draw":  #Solange kein Unentschieden
            another_one = input("---Draw!---\nDo you want to play another game? Y/N ") #Abfragen, ob neues Spiel gestartet werden soll
            if another_one == "Y" or another_one == "y":
                Singleplayer_Game()
            else:
                break

        if Next_Turn == "Player 1":   #Wenn als nächstes Spieler 1 dran ist
            Player  = "Player 1"      #Momentaner Spieler
            player_move(board, "X", Player, Turn_Count)   #Spieler 1 ist am Zug. Zeichen von Spieler 1 ist X
            Next_Turn = "Computer"   #Nächste Spieler, der dran ist
            Turn_Count += 1         #Zug um 1 erhöhen
            drawBoard(board)

        else:
            Player = "Computer"      #Momentaner Spieler
            player_move(board, "O", Player, Turn_Count)   #Spieler 2 ist am Zug. Zeichen von Spieler 2 ist 0
            Next_Turn = "Player 1"   #Nächste Spieler, der dran ist
            Turn_Count += 1         #Zug um 1 erhöhen
            drawBoard(board)

    else:
        print(Player + " Won!")  #Ausgeben, wer gewonnen hat
        another_one = input("Do you want to play another game? Y/N ")  #Abfragen, ob neues Spiel gestartet werden soll
        if another_one == "Y" or another_one == "y":
            Singleplayer_Game()
        else:
            pass


#Nimmt Input entgegen, prüft ob Zug möglich ist und führt diesen aus
def player_move(board, sign, Player, Turn_Count):
    if Player != "Computer":
        while True:
            try:    #try, da field mit einem nicht int konformen Wert zu einem Absturtz führt
                field = int(input("On which field do you want to place a {} {}? 1-9: ".format(sign, Player)))  #Auswählen auf welchem Feld das Zeichen gesetzt werden soll
            except ValueError: #Wenn field kein Int
                print("The field must be a Number between 1 and 9!")
                player_move(board, sign, Player)
                break #Springt nach drawBoard hierhin zurück. Ohne break gibt es einen Referenced before assigned error bei "if field < 1 or field > 9:""
        
            if field < 1 or field > 9:      #Wenn Feld auserhalb der Reichweite  
                print("Please Input a Number between 1 and 9 to choose your field. 1 for the top left and 9 for the bottom right.")
            elif board[field] != " ":       #Wenn schon ein Wert im Feld steht
                print("Theres already a {} in this Field. Please choose another one.".format(sign))
            else:
                pass   
            board[field] = sign #In Liste board momentanes Feld mit Zeichen beschreiben
            #drawBoard(board)
            break #Springt immer zum except zurück - WARUM?
    elif Turn_Count <= 1: #Wenn der erste Zug des Computer ist """COMPUTER MOVE"""
        field = random.randint(1, 9)    #Zufälligen Zug generieren
        while board[field] != " ":
            field = random.randint(1, 9)    #Zufällige Züge generieren, bis einer zulässig ist
        board[field] = sign #In Liste board momentanes Feld mit Zeichen beschreiben
            #drawBoard(board)
    else: 
        Win_detect(board)


#Algorithmus des Computers um Siege des Spielers zu verhindern und selbst zu gewinnen
def Win_detect(board):
    sign = "O"
    
    win = self_win(board)
    if win != False:
        board[win] = sign #Feld, dass zum Sieg führt besetzen 
    else:   #Wenn niergendwo zwei selbe Felder in einer Reihe sind #Eckfelder nach verfügbarkeit prüfen
        loose = opponent_win(board)
        if loose != False: # Wenn Gegenüber gewinnen könnte
            board[loose] = sign #Feld, dass zur Niederlage führt besetzen    
        else:
            if board[1] == " ":
                board[1] = sign
            elif board[3] == " ":
                board[3] = sign
            elif board[7] == " ":
                board[7] = sign
            elif board[9] == " ":
                board[9] = sign
            else:   #Falls auch das keinen Zug ergibt(Was eigentlich nicht möglich sein sollte, aber sicher ist sicher)
                field = random.randint(1, 9)    #Zufälligen Zug generieren
                while board[field] != " ":
                    field = random.randint(1, 9)    #Zufällige Züge generieren, bis einer zulässig ist
                board[field] = sign #In Liste board momentanes Feld mit Zeichen beschreiben


#Überprüft, ob der Spieler irgendwie gewinnen kann / TRUE - platziert Symbol / FALSE - returns False
def opponent_win(board):
    if board[1] == board[2] == "X" and board[3] == " " or board[2] == board[3] == "X" and board[1] == " " or board[3] == board[1] == "X" and board[2] == " ": #prüfen ob in Zeile 1 nur noch Feld zum Sieg fehlt:
        if board[3] == " ":                  #Wenn board[3] fehlt
            return 3
        elif board[1] == " ":                #Wenn board[1] fehlt
            return 1
        elif board[2] == " ":                #Wenn board[2] fehlt
            return 2
    elif board[4] == board[5] == "X" and board[6] == " " or board[5] == board[6] == "X" and board[4] == " " or board[6] == board[4] == "X" and board[5] == " ": #prüfen ob in Zeile 2 nur noch Feld zum Sieg fehlt:
        if board[6] == " ":                  #Wenn board[6] fehlt
            return 6
        elif board[4] == " ":                #Wenn board[4] fehlt
            return 4
        elif board[5] == " ":                #Wenn board[5] fehlt
            return 5
    elif board[7] == board[8] == "X" and board[9] == " " or board[8] == board[9] == "X" and board[7] == " " or board[9] == board[7] == "X" and board[8] == " ": #prüfen ob in Zeile 3 nur noch Feld zum Sieg fehlt:
        if board[9] == " ":                  #Wenn board[9] fehlt
            return 9
        elif board[7] == " ":                #Wenn board[7] fehlt
            return 7
        elif board[8] == " ":                #Wenn board[8] fehlt
            return 8
    #Spalten
    elif board[1] == board[4] == "X" and board[7] == " " or board[4] == board[7] == "X" and board[1] == " " or board[7] == board[1] == "X" and board[4] == " ": #prüfen ob in Spalte 1 nur noch Feld zum Sieg fehlt:
        if board[7] == " ":                  #Wenn board[7] fehlt
            return 7
        elif board[1] == " ":                #Wenn board[1] fehlt
            return 1
        elif board[4] == " ":                #Wenn board[4] fehlt
            return 4
    elif board[2] == board[5] == "X" and board[8] == " " or board[5] == board[8] == "X"and board[2] == " " or board[8] == board[2] == "X" and board[5] == " ": #prüfen ob in Spalte 2 nur noch Feld zum Sieg fehlt:
        if board[8] == " ":                  #Wenn board[8] fehlt
            return 8
        elif board[2] == " ":                #Wenn board[2] fehlt
            return 2
        elif board[5] == " ":                #Wenn board[5] fehlt
            return 5
    elif board[3] == board[6] == "X" and board[9] == " " or board[6] == board[9] == "X" and board[3] == " " or board[9] == board[3] == "X" and board[6] == " ": #prüfen ob in Spalte 3 nur noch Feld zum Sieg fehlt:
        if board[9] == " ":                  #Wenn board[9] fehlt
            return 9
        elif board[3] == " ":                #Wenn board[3] fehlt
            return 3
        elif board[6] == " ":                #Wenn board[6] fehlt
            return 6
    #Diagonal
    elif board[1] == board[5] == "X" and board[9] == " " or board[5] == board[9] == "X" and board[1] == " " or board[9] == board[1] == "X" and board[5] == " ": #prüfen ob in Spalte 2 nur noch Feld zum Sieg fehlt:
        if board[1] == " ":                  #Wenn board[1] fehlt
            return 1 
        elif board[5] == " ":                #Wenn board[5] fehlt
            return 5
        elif board[9] == " ":                #Wenn board[9] fehlt
            return 9
    elif board[3] == board[5] == "X" and board[7] == " " or board[5] == board[7] == "X" and board[3] == " " or board[7] == board[3] == "X" and board[5] == " ": #prüfen ob in Spalte 3 nur noch Feld zum Sieg fehlt:
        if board[3] == " ":                  #Wenn board[3] fehlt
            return 3
        elif board[5] == " ":                #Wenn board[5] fehlt
            return 5
        elif board[7] == " ":                #Wenn board[7] fehlt
            return 7
    else: 
        return False


#Überprüft, ob es irgendwo eine Moglichkeit gibt zu gewinnen %TRUE - platziert Symbol / FALSE - Platziert Symbol irgendwo in einer Ecke
def self_win(board):
    if board[1] == board[2] == "O" and board[3] == " " or board[2] == board[3] == "O" and board[1] == " " or board[3] == board[1] == "O" and board[2] == " ": #prüfen ob in Zeile 1 nur noch Feld zum Sieg fehlt:
        if board[3] == " ":                  #Wenn board[3] fehlt
            return 3
        elif board[1] == " ":                #Wenn board[1] fehlt
            return 1
        elif board[2] == " ":                #Wenn board[2] fehlt
            return 2
    elif board[4] == board[5] == "O" and board[6] == " " or board[5] == board[6] == "O" and board[4] == " " or board[6] == board[4] == "O" and board[5] == " ": #prüfen ob in Zeile 2 nur noch Feld zum Sieg fehlt:
        if board[6] == " ":                  #Wenn board[6] fehlt
            return 6
        elif board[4] == " ":                #Wenn board[4] fehlt
            return 4
        elif board[5] == " ":                #Wenn board[5] fehlt
            return 5
    elif board[7] == board[8] == "O" and board[9] == " " or board[8] == board[9] == "O" and board[7] == " " or board[9] == board[7] == "O" and board[8] == " ": #prüfen ob in Zeile 3 nur noch Feld zum Sieg fehlt:
        if board[9] == " ":                  #Wenn board[9] fehlt
            return 9
        elif board[7] == " ":                #Wenn board[7] fehlt
            return 7
        elif board[8] == " ":                #Wenn board[8] fehlt
            return 8
    #Spalten
    elif board[1] == board[4] == "O" and board[7] == " " or board[4] == board[7] == "O" and board[1] == " " or board[7] == board[1] == "O" and board[4] == " ": #prüfen ob in Spalte 1 nur noch Feld zum Sieg fehlt:
        if board[7] == " ":                  #Wenn board[7] fehlt
            return 7
        elif board[1] == " ":                #Wenn board[1] fehlt
            return 1
        elif board[4] == " ":                #Wenn board[4] fehlt
            return 4
    elif board[2] == board[5] == "O" and board[8] == " " or board[5] == board[8] == "O" and board[2] == " " or board[8] == board[2] == "O" and board[5] == " ": #prüfen ob in Spalte 2 nur noch Feld zum Sieg fehlt:
        if board[8] == " ":                  #Wenn board[8] fehlt
            return 8
        elif board[2] == " ":                #Wenn board[2] fehlt
            return 2
        elif board[5] == " ":                #Wenn board[5] fehlt
            return 5
    elif board[3] == board[6] == "O" and board[9] == " " or board[6] == board[9] == "O" and board[3] == " " or board[9] == board[3] == "O" and board[6] == " ": #prüfen ob in Spalte 3 nur noch Feld zum Sieg fehlt:
        if board[9] == " ":                  #Wenn board[9] fehlt
            return 9
        elif board[3] == " ":                #Wenn board[3] fehlt
            return 3
        elif board[6] == " ":                #Wenn board[6] fehlt
            return 6
    #Diagonal
    elif board[1] == board[5] == "O" and board[9] == " " or board[5] == board[9] == "O" and board[1] == " " or board[9] == board[1] == "O" and board[5] == " ": #prüfen ob in Spalte 2 nur noch Feld zum Sieg fehlt:
        if board[1] == " ":                  #Wenn board[1] fehlt
            return 1 
        elif board[5] == " ":                #Wenn board[5] fehlt
            return 5
        elif board[9] == " ":                #Wenn board[9] fehlt
            return 9
    elif board[3] == board[5] == "O" and board[7] == " " or board[5] == board[7] == "O" and board[3] == " " or board[7] == board[3] == "O" and board[5] == " ": #prüfen ob in Spalte 3 nur noch Feld zum Sieg fehlt:
        if board[3] == " ":                  #Wenn board[3] fehlt
            return 3
        elif board[5] == " ":                #Wenn board[5] fehlt
            return 5
        elif board[7] == " ":                #Wenn board[7] fehlt
            return 7
    else: 
        return False
