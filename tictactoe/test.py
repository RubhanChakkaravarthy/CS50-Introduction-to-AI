from tictactoe import X, O, EMPTY, terminal

board = [
    [EMPTY, O, X],
    [EMPTY, O, X],
    [EMPTY, EMPTY, X]
]

if terminal(board):
    print("true")