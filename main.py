from functions import *
user = 'X'
cpu = 'O'
win = False
validPos = [1,2,3,4,5,6,7,8,9]
board = [
        [' ', '|', ' ', '|', ' '],
        ['-', '+', '-', '+', '-'],
        [' ', '|', ' ', '|', ' '],
        ['-', '+', '-', '+', '-'],
        [' ', '|', ' ', '|', ' ']
]

while not win:
    printBoard(board)
    updateBoard(board, user, validPos)
    updateBoard(board, cpu, validPos)
