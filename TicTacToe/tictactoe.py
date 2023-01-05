print("<<<Tic-Tac Toe the game>>>\n""<<<Game by V.S.Voronov>>>\n""<<<Developed for DICT>>>\n")
board = ['-', '-', '-',
        '-', '-', '-',
        '-', '-', '-']
currentPlayer = "X"
winner = None
gameRunning = True


def printBoard(board):
    """Printing the board"""
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("-" * 9)
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("-" * 9)
    print(board[6] + " | " + board[7] + " | " + board[8])


def playerInput(board):
    """Take player input"""
    while True:
        if currentPlayer == "X":
            inp = int(input(f"Enter the number between 1-9 [X]: "))
        else:
            inp = int(input(f"Enter the number between 1-9 [0]: "))
        if inp >= 1 and inp <= 9 and board[inp-1] == "-":
            board[inp-1] = currentPlayer
            break
        else:
            if currentPlayer == "X":
                print(f"Player [X] this number has been used!")
            else:
                print(f"Player [0] this number has been used!")
            printBoard(board)


def checkHorizontal(board):
    global winner
    if (board[0] == board[1] == board[2] and board[0] != "-") or (board[3] == board[4] == board[5] and board[3] != "-") or (board[6] == board[7] == board[8] and board[6] != "-"):
        winner = currentPlayer
        return True
def checkRow(board):
    global winner
    if (board[0] == board[3] == board[6] and board[0] != "-") or (board[1] == board[4] == board[7] and board[1] != "-") or (board[2] == board[5] == board[8] and board[2] != "-"):
        winner = currentPlayer
        return True
def checkDiagonal(board):
    global winner
    if (board[0] == board[4] == board[5] and board[0] != "-") or (board[2] == board[4] == board[6] and board[2] != "-"):
        winner = currentPlayer
        return True
def checkTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("Draw, play again.")
        gameRunning = False

def checkWin():
    """Check for win or draw"""
    if checkDiagonal(board) or checkHorizontal(board) or checkRow(board):
        print(f"The winner is {winner}")


def switchPlayer():
    """Switch the player"""
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"


while gameRunning:
    """Check for win or draw again"""
    printBoard(board)
    if winner != None:
        break
    playerInput(board)
    checkWin()
    checkTie(board)
    switchPlayer()