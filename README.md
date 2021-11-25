# Tic-Tac-Toe-Python

## Game

![Game](https://github.com/KiShiVi/Tic-Tac-Toe-Python/blob/main/media/gameExample.gif)

## Description

Comic project - tic-tac-toe, written in python. 

Allows you to play a game of tic-tac-toe with a real opponent on the same host. 

The players themselves determine the size of the field and the number of cells for winning.

## API

### TicTacToe constructor
```TicTacToe(a, b, player1, player2, countOfCellForWin)``` - constructor for creating a __TicTacToe__ object  

___a :Int___ - field width _(1..26)_

___b :Int___ - field height _(1..26)_

___player1 :Player___ - first player

___player2 :Player___ - second player

___countOfCellForWin :Int___ - number of cells to win _(Default: 3)_

### Player constructor

```Player(name)``` - constructor for creating a __Player__ object 

___name :String___ - player name

### API for the game

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
