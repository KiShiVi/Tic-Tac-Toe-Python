from tic_tac_toe import Player
from tic_tac_toe import TicTacToe

print("Welcome to TicTacToe game!")
print("Input field size: ")

filedSize = list(map(int, input().split()))

print("Player 1 - please introduce yourself:")
player1 = Player(input())
print("Player 2 - please introduce yourself:")
player2 = Player(input())
print("Number of cells to win:")
countOfCellForWin = int(input())

gameObj = TicTacToe(filedSize[0], filedSize[1], player1, player2, countOfCellForWin)
gameObj.game()

