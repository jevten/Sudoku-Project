from sudoku_generator import SudokuGenerator
from cell import Cell
import pygame

class Board():
    #constructor for the board class
    def __init__(self, width, height, screen, difficulty):
        #create the list of cells object for the board
        self.list_of_cells =[[0 for x in range(0,9)]for y in range(0,9)]
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        #9 squares sizes
        self.SQUARE_SIZE_VERT = int(600/3)
        self.SQUARE_SIZE_HORZ = int(600/3)
        #color of board lines
        self.LINE_COLOR_BOX = (0, 0, 0)
        self.LINE_COLOR_CELL = (242, 158, 22)
        self.LINE_COLOR_SELECT = (232, 5, 16)
        #create board using class method based upond diffuctly entered
        if difficulty == "easy":
            self.board = SudokuGenerator(9,30)
        if difficulty == "medium":
            self.board = SudokuGenerator(9,40)
        if difficulty == "hard":
            self.board = SudokuGenerator(9,50)
        #create the board by filling the values using class method a removign them
        self.board.fill_values()
        self.board.remove_cells()
        #create the list of cells with each cell object by iterating through the empty 9x9 list
        for i in range(0,9):
            for j in range(0,9):
                self.list_of_cells[i][j] = Cell(self.board.get_board()[i][j], i, j ,self.screen)
        self.selected_cell = (0,0)
        #create a copy of the original board by iterzating through each cell value at the column and row
        self.original_board = [[0 for x in range(0,9)]for y in range(0,9)]
        for i in range(0,9):
            for j in range(0,9):
                self.original_board[i][j] = self.board.get_board()[i][j]


    #function to draw the board
    def draw(self):
        #draw the 8 vertical and horizontal lines to distinguish the different cells
        for i in range(1,9):
            pygame.draw.line(self.screen, self.LINE_COLOR_CELL, (0,i*600/9),(self.width, i*600/9),2)
        for i in range(1,9):
            pygame.draw.line(self.screen,self.LINE_COLOR_CELL,(i * 600/9,0), (600/9 * i, self.height),3)
        #draw three thicker black horizontal and vertical lines to distinguish the boxes
        for i in range(0, 4):
            pygame.draw.line(self.screen, self.LINE_COLOR_BOX, (0, i * self.SQUARE_SIZE_VERT), (self.width, i * self.SQUARE_SIZE_VERT), 5)
        for i in range(0, 4):
            pygame.draw.line(self.screen, self.LINE_COLOR_BOX, (i * self.SQUARE_SIZE_HORZ,0), (self.SQUARE_SIZE_HORZ * i, self.height), 5)
        #draw each of the cells values on the baord using cell class value in according spot
        for i in range (0,9):
            for j in range(0,9):
                self.list_of_cells[i][j].draw()

        #function to return list of cell objects
        def get_list_of_cells():
            return self.list_of_cells

    # function to select a cell on the board
    def select(self, row, col):
        #draw red lines around the box to show the user what cell they selected
        for i in range(0,2):
            pygame.draw.line(self.screen,self.LINE_COLOR_SELECT,(col*600/9,(row + i)*600/9),(600/9*(col+1), (row + i)*600/9),2)
        for i in range(0, 2):
            pygame.draw.line(self.screen, self.LINE_COLOR_SELECT, ((col + i) * 600 / 9, row * 600 / 9),(600/9*(col+i),(row+1)*600/9),2)
        #store the selected value for it to be changed
        self.selected_cell = (row,col)

    #function to determine the row and col of the click based on the screen size
    def click(self, x, y):
        if x>600 and x<0 and y>700 and y<0:
            return None
        row = 0
        col = 0
        #knowing the board is 600x600 use correct math to determine the row and col of the click
        for i in range(0,9):
            if x>=600/9*i and x<=600/9*(i+1):
                col = i
            if y >= 600 / 9 * i and y <= 600 / 9 * (i + 1):
                row=i
        result = (row,col)
        return result

    # function to clear the value in the selected cell by setting it to zero
    def clear(self):

        i, j = self.selected_cell
        self.list_of_cells[i][j] = Cell(0,i,j,self.screen)

    # function to sketch the value entered in a cell by user
    def sketch(self,value):
        i, j = self.selected_cell
        #ensure user cant change given value
        if self.original_board[i][j] >0:
            return None
        #set the sketched to the one entered
        self.list_of_cells[i][j].set_sketched_value(value)
        #use class method to display sketched value on board
        self.list_of_cells[i][j].draw_sketched_value()

    #function to draw the value of the cell on the board
    def place_number(self,value):
        i, j = self.selected_cell
        #ensure no to display and empty cell value on the board
        if self.original_board[i][j] >0:
            return None
        #set the real value of the cell to value given in parameters
        self.list_of_cells[i][j].set_cell_value(value)
        #draw the value of the board using class method
        self.list_of_cells[i][j].draw()

    #function to reset board to the orignal values created
    def reset_to_original(self):
        #iterate through list of cells and change the values according only the original board value lsit
        for i in range(0,9):
            for j in range(0,9):
                self.list_of_cells[i][j] = self.original_board[i][j]

    #function to check if the board is full
    def is_full(self):
        count = 0
        #iterate through the list of cells checking if all the values are greater than 1
        for i in range(0,9):
            for j in range(0,9):
                if self.list_of_cells[i][j].get_value() == 0:
                    count+=1
        # if any 1 cell is valued at 0 return board is not full
        if count >0:
            return False
        return True

    #function to update underlying list to the entered values in the game
    def update_board(self):
        #iterate through the board and set the underlying list to the list being hcanged in game
        for i in range(0,9):
            for j in range(0,9):
                self.board.get_board()[i][j] = self.list_of_cells[i][j].get_value()
        self.board.print_board()

    #function to find an empty cell on the board
    def find_empty(self):
        #iterate through the list of values on the baord
        for i in range(0,9):
            for j in range(0,9):
                #check for a value of zero
                if self.list_of_cells[i][j].get_value()==0:
                    result = (i,j)
                    #reutnr location of the empty cell
                    return result
        return None

    #function to check if the board is correctly or incorrectly filled out
    def check_board(self):
        # Check rows
        for row in self.board.get_board():
            if set(row) != set(range(1, 10)):
                return False

        # Check columns
        for col in range(9):
            if set(self.board.get_board()[row][col] for row in range(9)) != set(range(1, 10)):
                return False

        # Check subgrids
        for row_start in range(0, 9, 3):
            for col_start in range(0, 9, 3):
                subgrid = [
                    self.board.get_board()[row][col]
                    for row in range(row_start, row_start + 3)
                    for col in range(col_start, col_start + 3)
                ]
                if set(subgrid) != set(range(1, 10)):
                    return False

        return True




