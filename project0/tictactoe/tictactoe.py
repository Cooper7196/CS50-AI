"""
Tic Tac Toe Player
"""

import math

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
    xCount = 0
    oCount = 0
    for row in board:
          xCount += row.count(X)
          oCount += row.count(O)
    if (xCount + oCount) % 2 == 0:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possibleActions = []
    for row in range(len(board)):
        for pos in range(len(board[row])):
            if board[row][pos] == None:
                possibleActions.append((row,pos))
    return possibleActions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board[action[0]][action[1]] = player(board)
    return board
    


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    #Check if any rows has only Xs or Os
    for row in board:
        if set(row) == set(X):
            return X
        elif set(row) == set(O):
            return O

    #Check if any columns has only Xs or Os
    for column in range(len(board)):
        columnSet = set([board[row][column] for row in range(len(board[0]))])
        if columnSet == set(X):
            return X
        elif columnSet == set(O):
            return O
   
    #Check if any diagonals has only Xs or Os
    diagonalTopLeftToRight = set([board[i][i] for i in range(len(board))])
    if diagonalTopLeftToRight == set(X):
        return X
    elif diagonalTopLeftToRight == set(O):
        return O
    
    diagonalBottomLeftToRight = set([board[(len(board) - 1) - i][i] for i in range(len(board) - 1, -1, -1)])
    if diagonalBottomLeftToRight == set(X):
        return X
    elif diagonalBottomLeftToRight == set(O):
        return O

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return all([None not in row for row in board]) or winner(board) is not None


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    
    return 0 if winner(board) == None else 1 if winner(board) == X else -1


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
