from tictactoe import *

board = [[None, None, None], [None, None, None], [None, None, None]]
print(board)

board = result(board, (0, 0))

print(board)

board = result(board, (0, 1))

print(board)

board = [[X,X,X],[X,X,X],[X,X,None]]

print(terminal(board))
