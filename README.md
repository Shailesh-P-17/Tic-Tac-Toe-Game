# Tic-Tac-Toe-Game

# About
Tic Tac Toe is a simple game that is played by two players. The game is played on a 3x3 grid. The players take turns placing their symbol (either "X" or "O") in an empty cell. The first player to get three of their symbols in a row (horizontally, vertically, or diagonally) wins the game. If all cells are filled and no one has won, the game is tied.

# Guided Path
Check out our guided path on Tic Tac Toe for more information on the development process and our thoughts on the Tic Tac Toe Game project:

Tic Tac Toe Game Using Python.
3 Requirements
Python 3.x
Tkinter library (which is usually included with Python)
# Getting Started
 1. Clone this repository to your local machine.
 2. Launch Jupyter Notebook.
 3. Then navigate to the cloned repository.
# How to Play
 1.The game is played on a 3x3 grid.
 2.The players take turns placing their symbol (either "X" or "O") in an empty cell.
 3.The first player to get three of their symbols in a row (horizontally, vertically, or diagonally) wins the game.
 4.If all cells are filled, and no one has won, the game is tied.
# Code Structure
The code is organized into a single class, TicTacToe, which contains the following methods:
 1. __init__(self, master) : This method initializes the game window, sets up the game board, and creates the buttons for the game board.

 2. handle_click(self, row, col) : This method is called when a player clicks on a cell in the game board. It updates the game board and checks if the game is over (i.e. if a player has won or the game is tied).

 3. switch_player(self) : This method alternates between "X" and "O" after each move.

 4. check_win(self) : This method checks if any player has won the game by getting three of their symbols in a row.

 5. check_tie(self) : This method checks if the game is tied (i.e. all cells are filled and no one has won).

 6. game_over(self) : This method disables all buttons and displays a message announcing the winner or declaring a tie.

