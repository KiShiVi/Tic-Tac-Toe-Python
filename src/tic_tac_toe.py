from enum import Enum

ABC = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']


class Flag(Enum):
    NULL = 0
    NOUGHT = 1
    CROSS = 2


class Player:
    def __init__(self, name="Player", mark=Flag.NULL):
        self.name = name
        self.mark = mark


class TicTacToe:
    def __init__(self, a, b, player1, player2):
        self.a = a
        self.b = b
        self.field = [[Flag.NULL for j in range(a)] for i in range(b)]
        self.player1 = Player(player1.name, Flag.NOUGHT)
        self.player2 = Player(player2.name, Flag.CROSS)
        self.turn = self.player1

    def turn(self, x, y, player):
        if self.field[y][x] == Flag.NULL:
            return None
        self.field[y][x] = player.mark
