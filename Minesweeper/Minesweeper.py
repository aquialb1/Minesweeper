import random

class Board():
    def __init__(self, dim_size, num_mines):
        # board parameters
        self.dim_size = dim_size
        self.num_mines = num_mines
        
        self.board = self.make_new_board()
        self.assign_board_values()

        # initalize loc coordinates (row,column) as empty set
        self.dug = set()
        
    def make_new_board(self):
        # creates new board based on dim size
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        
        # plant mines
        mines_planted = 0
        while mines_planted < self.num_mines:
            loc = random.randint(0,self.dim_size**2 - 1)    # returns random int N so that a <= N <= b
            row = loc // self.dim_size      # get row based on number of times dim_size goes into loc
            col = loc % self.dim_size       # get column based on remainder
            
            # contine if mine is already planted at loc
            if board[row][col] == '*':
                continue
            
            board[row][col] = '*'
            mines_planted += 1
            
        return board
    
    def assign_board_values(self):
        # assign a value 0-8 for all empty spaces, representing # of neighboring mines
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                # if loc is already a mine, don't calculate
                if self.board[r][c] == '*':
                    continue
                
                self.board[r][c] == self.get_neighboring_mines(r, c)
                
    def get_neighboring_mines(self, row, col):
        # iterate through each neighboring position and sum # of mines
        num_neighboring_mines = 0
        # bounds checking
        for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                # don't check if original location
                if r == row and c == col:
                    continue
                
                if self.board[r][c] == '*':
                    num_neighboring_mines += 1
                    
        return num_neighboring_mines
    
    def dig(self, row, col):
        self.dug.add((row, col))    # keep track of dig loc
        
        # return false if mine is dug, return true if not
        if self.board[row][col] == '*':
            return False
        elif self.board[row][col] > 0:      # dug at loc w/ neighboring mines
            return True
        
        # if board loc is = to 0
        for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                if (r, c) in self.dug:
                    continue    # don't dig if loc is already dug
                self.dig(r, c)
                
        return True
    
    def __str__(self):
        # generate array to visualize board
        pass

def play(dim_size = 10, num_mines = 10):
    # generate board
    board = Board(dim_size, num_mines)
    

