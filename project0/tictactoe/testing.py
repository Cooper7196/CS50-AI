from tictactoe import *

board = [[None, None, None], [None, None, None], [None, None, None]]
print(board)

board = result(board, (0, 0))

print(board)

board = result(board, (0, 1))

print(board)

board = [[None,O,X],[None,O,O],[X,X,O]]

print(terminal(board))
print(board)
print(f"Winner: {winner(board)}")
print(f"Utility: {utility(board)}")