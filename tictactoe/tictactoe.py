"""
Tic Tac Toe Player
"""
import math
import random
from copy import deepcopy

import util

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    num = [0, 0]
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                num[0] += 1
            elif board[i][j] == O:
                num[1] += 1

    return X if num[0] == num[1] else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions_set = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions_set.add((i, j))

    return actions_set


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # copy the board so no mutation happens when working with other nodes
    board_copy = deepcopy(board)
    i, j = action
    board_copy[i][j] = player(board_copy)

    return board_copy



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    Winner = None

    # rows and column check
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0]:
            Winner = board[i][0]
            break
        if board[0][i] == board[1][i] == board[2][i] and board[0][i]:
            Winner = board[0][i]
            break

    # diagonal check
    if not Winner:
        if board[0][0] == board[1][1] == board[2][2] and board[0][0]:
            Winner = board[0][0]
        elif board[0][2] == board[1][1] == board[2][0] and board[0][2]:
            Winner = board[0][2]

    return Winner


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # if there is a winner or no moves left
    if winner(board) or len(actions(board)) == 0:
        return True

    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    Winner = winner(board)

    if Winner == X:
        return 1
    elif Winner == O:
        return -1
    else:
        return 0

# Alpha is the maximum score of the parent calculated upto current child
# Beta is the minimum score of the parent calculated upto that current child

def max_value(board, alpha, beta):  
    if terminal(board):
        return utility(board)

    v = -math.inf
    actions_set = actions(board)
    for action in actions_set:
        # Alpha Beta Pruning
        # Compare with parent score
        # if it is greater than parent score or beta then
        # the parent min will never select this child action
        alpha = max(alpha, min_value(result(board, action), alpha, beta))
        if alpha > beta:
            return beta
        v = max(v, alpha)

    return v # or beta

def min_value(board, alpha, beta): 
    if terminal(board):
        return utility(board)

    v = math.inf
    actions_set = actions(board)
    # for every child action
    for action in actions_set:
        # Alpha Beta Pruning
        # Compare with parent score or alpha
        # if it is lesser than parent score or alpha then
        # the parent max will never select this child action
        beta = min(beta, max_value(result(board, action), alpha, beta))
        if beta < alpha:
            return beta
        v = min(v, beta)

    return v # or Alpha

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        print("Already game over")
    actions_set = actions(board)

    if len(actions_set) == 9:
        return random.choice(list(actions_set))

    action_score_pair = []
    current_player = player(board)

    alpha = -math.inf
    beta = math.inf

    if current_player == X:
        for action in actions_set:
            score = min_value(result(board, action), alpha, beta)
            action_score_pair.append((action, score))
        return util.max_score_action(action_score_pair)

    elif current_player == O:
        for action in actions_set:
            score = max_value(result(board, action), alpha, beta)
            action_score_pair.append((action, score))
        return util.min_score_action(action_score_pair)



