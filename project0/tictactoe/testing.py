from tictactoe import *

board = initial_state()
board = [[X, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY],[O, EMPTY, EMPTY]]
# while True:
print(board)
print(minimax_value(board))
# board = result(board, minimax(board))
