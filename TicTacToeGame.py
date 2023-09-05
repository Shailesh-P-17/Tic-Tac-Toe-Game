import tkinter as tk
from tkinter import messagebox

class TicTacToeGame:
    
    
    # Initialization of Tic Tac Toe class
    def __init__(self):
        
        # we start with the current player set to "X", that means "X" will be the first to play 
        self.current_player = "X"
        
        # we created 3x3 matrix board initially, all positions on the board are empty(string)
        self.board = [["" for _ in range(3)]for _ in range(3)]
        
        # create a Tkinter window ,the graphical interface for the game and set its title to "Tic Tac Toe Game"
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe Game")
        
        # we use nested loops to create a 3x3 grid of buttons for the game board
        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                # each button is associated with make_move() function using a lambda function
                # this allows us to handle button clicks and call the make_move function with corresponding row and column indics.
                button = tk.Button(self.window, text="", width=30, height=15, command=lambda i=i,j=j:self.make_move(i, j))
                # we display the buttons on the Tkinter window using the grid method 
                button.grid(row=i, column=j)
                row.append(button)
                # we store references to the buttons in the self. buttons list for easy access later
            self.buttons.append(row)
    
    
    def make_move(self, row, col):
        
        # the function checks if the clicked position on the board is empty 
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            
            # it checks if the current player has wonby calling the check_winner function
            if self.check_winner(self.current_player):
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.window.quit()
            
            # if there's no win the function checks if the board is full by calling the is_board_full function.
            elif self.is_board_full():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.window.quit()
            
            # it switches the current player to next one
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
    
    
    
    def check_winner(self, player):
        
        # In order to determine if there is a winning conditionin Tic Tac Toe game
        # we need to check each row,column and diagonal of the game board
        for i in range(3):
            
            # first,we'll iterate over each row
            if self.board[i][0] == self.board[i][1] == self.board[i][2] == player:
                return True
            # next, we move on to checking the columns 
            if self.board[0][i] == self.board[1][i] == self.board[2][i] == player:
                return True
        
        # after checking rows and columns, we examine the diagonals
        # the top-left to boottom-right diagonal.
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == player:
            return True
        
        # the top-right to bottom-left diagonal.
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == player:
            return True
        return False
    
    
    
    def is_board_full(self):
        
        # checking for board blocks full or empaty.
        for row in self.board:
            if "" in row:
                return False
        
        return True
    
    # run fuction
    def run(self):
        self.window.mainloop()

# derived code
game = TicTacToeGame()
game.run()
