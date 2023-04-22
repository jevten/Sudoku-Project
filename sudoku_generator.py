import math,random

"""
This was adapted from a GeeksforGeeks article "Program for Sudoku Generator" by Aarti_Rathi and Ankur Trisal
https://www.geeksforgeeks.org/program-sudoku-generator/

"""

class SudokuGenerator:
    '''
	create a sudoku board - initialize class variables and set up the 2D board
	This should initialize:
	self.row_length		- the length of each row
	self.removed_cells	- the total number of cells to be removed
	self.board			- a 2D list of ints to represent the board
	self.box_length		- the square root of row_length

	Parameters:
    row_length is the number of rows/columns of the board (always 9 for this project)
    removed_cells is an integer value - the number of cells to be removed

	Return:
	None
    '''
    #constructor for the class
    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells
        #length of the 9 boxes on the board
        self.box_length = int(math.sqrt(self.row_length))
        #2d list initalization for the board
        self.board = [[0 for _ in range(row_length)]for _ in range(row_length)]


    '''
	Returns a 2D python list of numbers which represents the board

	Parameters: None
	Return: list[list]
    '''
    def get_board(self):
        #reutrn the board list
        return self.board

    '''
	Displays the board to the console
    This is not strictly required, but it may be useful for debugging purposes

	Parameters: None
	Return: None
    '''
    def print_board(self):
        #print board in sudoku format by iterating through each element in each list
        for i in range(self.row_length):
            for j in range(self.row_length):
                print(self.board[i][j], end=" ")
            print()

    '''
	Determines if num is contained in the specified row (horizontal) of the board
    If num is already in the specified row, return False. Otherwise, return True

	Parameters:
	row is the index of the row we are checking
	num is the value we are looking for in the row
	
	Return: boolean
    '''
    #function to check if a number is valid in the row it will be placed in
    def valid_in_row(self, row, num):
        #iterate though the row by changing second element in the list checking if a number is equal
        for i in range(self.row_length):
            if num == self.board[row][i]:
                return False
        return True

    '''
	Determines if num is contained in the specified column (vertical) of the board
    If num is already in the specified col, return False. Otherwise, return True

	Parameters:
	col is the index of the column we are checking
	num is the value we are looking for in the column
	
	Return: boolean
    '''
    #function to check if a number is valid in its column
    def valid_in_col(self, col, num):
        #iterate though the column by changing first element in the list checking if a number is equal
        for i in range(self.row_length):
            if num == self.board[i][col]:
                return False
        return True

    '''
	Determines if num is contained in the 3x3 box specified on the board
    If num is in the specified box starting at (row_start, col_start), return False.
    Otherwise, return True

	Parameters:
	row_start and col_start are the starting indices of the box to check
	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)
	num is the value we are looking for in the box

	Return: boolean
    '''
    #function to check if a number is valid in its box on the board, 9 boxes 3x3
    def valid_in_box(self, row_start, col_start, num):
        #start by ensuring that the check starts on the first value in the box
        if row_start > 3 and row_start < 6:
            row_start = 3
        if row_start > 0 and row_start < 3:
            row_start = 0
        if row_start > 6 and row_start < 9:
            row_start = 6
        if col_start > 0 and col_start < 3:
            col_start = 0
        if col_start > 3 and col_start < 6:
            col_start = 3
        if col_start > 6 and col_start < 9:
            col_start = 6
        #once the first value is selected iterate though the box using the box length and checking if equal
        for i in range(self.box_length):
            for j in range(self.box_length):
                if self.board[row_start+i][col_start+j] == num:
                    return False
        return True

    
    '''
    Determines if it is valid to enter num at (row, col) in the board
    This is done by checking that num is unused in the appropriate, row, column, and box

	Parameters:
	row and col are the row index and col index of the cell to check in the board
	num is the value to test if it is safe to enter in this cell

	Return: boolean
    '''
    #function to determine if a single elment is valid
    def is_valid(self, row, col, num):
        #use all the valid tests, if one returns false then the value is not valid
        if self.valid_in_box(row,col,num) == False:
            return False
        if self.valid_in_row(row,num) == False:
            return False
        if self.valid_in_col(col,num) == False:
            return False
        return True

    '''
    Fills the specified 3x3 box with values
    For each position, generates a random digit which has not yet been used in the box

	Parameters:
	row_start and col_start are the starting indices of the box to check
	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)

	Return: None
    '''
    #function to fill boxes when initializing board
    def fill_box(self, row_start, col_start):
        value = 0
        #iterate through the rows and cols in the box
        for i in range(int(self.box_length)):
            for j in range(int(self.box_length)):
                while True:
                    #create rnadom number 1-9
                    value = random.randint(1,9)
                    if self.valid_in_box(row_start,col_start,value):
                        break
                #add the random int 1-9 if the value is valid
                self.board[row_start + i][col_start + j] = value

    
    '''
    Fills the three boxes along the main diagonal of the board
    These are the boxes which start at (0,0), (3,3), and (6,6)

	Parameters: None
	Return: None
    '''
    #function to fill the box diagnoally
    def fill_diagonal(self):
        #using a for loop the steps up the box length every iteration to fill boxes diagnolly rather then every box
        for i in range(0, self.row_length, int(self.box_length)):
            self.fill_box(i,i)


    '''
    DO NOT CHANGE
    Provided for students
    Fills the remaining cells of the board
    Should be called after the diagonal boxes have been filled
	
	Parameters:
	row, col specify the coordinates of the first empty (0) cell

	Return:
	boolean (whether or not we could solve the board)
    '''
    def fill_remaining(self, row, col):
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True
        
        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    '''
    DO NOT CHANGE
    Provided for students
    Constructs a solution by calling fill_diagonal and fill_remaining

	Parameters: None
	Return: None
    '''
    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    '''
    Removes the appropriate number of cells from the board
    This is done by setting some values to 0
    Should be called after the entire solution has been constructed
    i.e. after fill_values has been called
    
    NOTE: Be careful not to 'remove' the same cell multiple times
    i.e. if a cell is already 0, it cannot be removed again

	Parameters: None
	Return: None
    '''
    #function to remove values after a board is made
    def remove_cells(self):
        count = self.removed_cells
        #randomly select values for the rows and cols to remove values if a vlue is already 0 it is checked and not removed again
        while count !=0:
            x = random.randint(0,8)
            y = random.randint(0,8)
            if self.board[x][y] != 0:
                count -=1
                self.board[x][y] = 0

'''
DO NOT CHANGE
Provided for students
Given a number of rows and number of cells to remove, this function:
1. creates a SudokuGenerator
2. fills its values and saves this as the solved state
3. removes the appropriate number of cells
4. returns the representative 2D Python Lists of the board and solution

Parameters:
size is the number of rows/columns of the board (9 for this project)
removed is the number of cells to clear (set to 0)

Return: list[list] (a 2D Python list to represent the board)
'''
def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board
