from tic_tac_toe import Player

print("Welcome to TicTacToe game!")
print("Input field size: ")

filedSize = list(map(int, input().split()))

print("Player 1 - please introduce yourself:")
player1 = Player(input())
print("Player 2 - please introduce yourself:")
player2 = Player(input())