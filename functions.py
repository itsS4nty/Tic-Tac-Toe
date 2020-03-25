from random import shuffle
def printBoard(board):
    for c in board:
        for i in c:
            print(i, end='')
        print()

def updateBoard(board, symbol, validPos):
    valid = False
    while not valid:
        if symbol == 'X':
            pos = int(input("Enter a position (1-9): "))
        else:
            shuffle(validPos)
            pos = validPos[0]
        if pos in validPos:
            valid = True
            if pos == 1:
                board[0][0] = symbol
            elif pos == 2:
                board[0][2] = symbol
            elif pos == 3:
                board[0][4] = symbol
            elif pos == 4:
                board[2][0] = symbol
            elif pos == 5:
                board[2][2] = symbol
            elif pos == 6:
                board[2][4] = symbol
            elif pos == 7:
                board[4][0] = symbol
            elif pos == 8:
                board[4][2] = symbol
            elif pos == 9:
                board[4][4] = symbol
            validPos.remove(pos)
        else:
            if pos >= 1 and pos <= 9:
                print("This position has been taken. Enter another one.")
            else:
                print("Enter a valid position (1-9)")
