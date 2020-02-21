#Funktionsbibliothek für TicTacToe
#Ersteller: Tobias Dominik Weber aka. MisterNSA 
#Version: 0.4 Datum: 21.02.2020


#Zeigt das Feld an
def drawBoard(board):                                                    
    print(" " + board[1] + " | " + board[2] + " | " + board[3])     
    print("-----------")
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print("-----------")
    print(" " + board[7] + " | " + board[8] + " | " + board[9])


#Nimmt Input entgegen, prüft ob Zug möglich ist und führt diesen aus
def player_move(board, sign):
    while True:
        field = int(input("On which field do you want to place a {}? 1-9".format(sign)))  #Auswählen auf welchem Feld das Zeichen gesetzt werden soll
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

#Überprüft, ob Jemand das Spiel gewonnen hat (Spielername + Won | True), alle Felder belegt wurden (Draw | "Draw"), oder es noch Zugmöglichkeiten gibt(False). 
def Win():


def 