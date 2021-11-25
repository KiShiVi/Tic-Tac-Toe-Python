# Tic-Tac-Toe-Python

## Game

![Game](https://github.com/KiShiVi/Tic-Tac-Toe-Python/blob/main/Media/gameExample.gif)

## Description

Comic project - tic-tac-toe, written in python. 

Allows you to play a game of tic-tac-toe with a real opponent on the same host. 

The players themselves determine the size of the field and the number of cells for winning.

## API

###TicTacToe constructor
```TicTacToe(a, b, player1, player2, countOfCellForWin)``` - constructor for creating a __TicTacToe__ object  

_a_ __:Int__ - field width _(1..26)_

_b_ __:Int__ - field height _(1..26)_

_player1_ __:Player__ - first player

_player2_ __:Player__ - second player

_countOfCellForWin_ __:Int__ - number of cells to win _(Default: 3)_

###Player constructor
```Player(name)``` - constructor for creating a __Player__ object 

_name_ __:String__ - player name

###API for the game

```TicTacToeObj.game()``` - launches the game

## Code Run Examples

```
from tic_tac_toe import Player
from tic_tac_toe import TicTacToe

# Launch of the classic 3x3 TicTacToe
gameObj = TicTacToe(3, 3, Player('Ivan'), Player('Alex'), 3) 
gameObj.game()
```
## Notes
- The program does not use third-party libraries
- A console game 