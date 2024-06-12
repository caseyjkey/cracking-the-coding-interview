# Design an algorithm to decide if someone has won tic-tac-toe
board = [1, 0, 0, 1, 0, 0, 1, 0, 0]


def isWinner(board, player):
    return any( player == board[a] == board[b] == board[c]
               for a, b, c in [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7),
                               (2, 5, 8), (0, 4, 8), (2, 4, 6)])

print(isWinner(board, 1))
