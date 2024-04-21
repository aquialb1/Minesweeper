import random

class Board():
    def __init__(self,dim_size,num_mines):
        # board parameters
        self.dim_size = dim_size
        self.num_mines = num_mines
        
        self.board = self.make_new_board()

        # initalize coordinates (row,column) as empty set
        self.dug = set()
        
    def make_new_board(self):
        # creates new board based on dim size
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        
        # plant mines
        mines_planted = 0
        while mines_planted < self.num_mines:
            loc = random.randint(0,self.dim_size**2 - 1)
            row = loc // self.dim_size
            col = loc % self.dim_size
            
            if board[row][col] == '*':
                continue
            
            board[row][col] = '*'
            mines_planted += 1
            
        return board

def play(dim_size = 10,num_mines = 10):
    pass
