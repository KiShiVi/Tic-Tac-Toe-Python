from enum import Enum

ABC = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
ABCForDraw = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']


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
        self.notTurn = self.player2

    def playerTurn(self, x, y, playerTurn, playerNotTurn):
        if self.field[y][x] != Flag.NULL:
            return None
        self.field[y][x] = playerTurn.mark
        self.turn, self.notTurn = playerNotTurn, playerTurn
        return True

    def isWin(self):
        for y in range(self.b):
            for x in range(self.a):
                if self.field[y][x] == Flag.NULL:
                    continue

                if self.isHorizontalLineWin(x, y) != Flag.NULL:
                    return self.isHorizontalLineWin(x, y)
                if self.isVerticalLineWin(x, y) != Flag.NULL:
                    return self.isVerticalLineWin(x, y)
                if self.isDiagonalsLeftLineWin(x, y) != Flag.NULL:
                    return self.isDiagonalsLeftLineWin(x, y)
                if self.isDiagonalsRightLineWin(x, y) != Flag.NULL:
                    return self.isDiagonalsRightLineWin(x, y)
        return Flag.NULL

    def isHorizontalLineWin(self, x, y):
        mark = self.field[y][x]
        result = 0
        for cell in self.field[y]:
            if result >= 3:
                return mark
            if cell == mark:
                result += 1
            else:
                result = 0
        if result >= 3:
            return mark
        return Flag.NULL

    def isVerticalLineWin(self, x, y):
        mark = self.field[y][x]
        result = 0
        for cell in self.field:
            if result >= 3:
                return mark
            if cell[x] == mark:
                result += 1
            else:
                result = 0
        if result >= 3:
            return mark
        return Flag.NULL

    def isDiagonalsLeftLineWin(self, x, y):
        mark = self.field[y][x]
        result = 0
        while x > 0 and y > 0:
            x -= 1
            y -= 1

        while (x < (self.a - 1)) and (y < (self.b - 1)):
            if result >= 3:
                return mark
            if self.field[y][x] == mark:
                result += 1
            else:
                result = 0
            x += 1
            y += 1
        if result >= 3:
            return mark
        return Flag.NULL

    def isDiagonalsRightLineWin(self, x, y):
        mark = self.field[y][x]
        result = 0
        while (x < (self.a - 1)) and (y < (self.b - 1)):
            x += 1
            y += 1

        while x > 0 and y > 0:
            if result >= 3:
                return mark
            if self.field[y][x] == mark:
                result += 1
            else:
                result = 0
            x -= 1
            y -= 1
        if result >= 3:
            return mark
        return Flag.NULL

    def game(self):
        while self.isWin() == Flag.NULL:
            self.drawField()
            self.checkTurn()
        status = self.isWin()
        self.drawField()
        if status == Flag.NOUGHT:
            print(self.player1.name + " is WIN!")
        else:
            print(self.player2.name + " is WIN!")

    def checkTurn(self):
        print(self.turn.name + ": Your turn! Input X and Y")
        x, y = input().split()
        if self.playerTurn(ABC[x], int(y) - 1, self.turn, self.notTurn) is None:
            print(self.turn.name + ": Your turn is wrong. Tru again")
            self.checkTurn()

    def drawField(self):
        print(" |", end='')
        for i in range(self.a):
            print(ABCForDraw[i] + "|", end='')
        for i in range(self.b):
            print('\n' + str(i + 1) + '|', end='')
            for j in self.field[i]:
                if j == Flag.NOUGHT:
                    print('O|', end='')
                elif j == Flag.CROSS:
                    print('X|', end='')
                else:
                    print(' |', end='')
        print()
