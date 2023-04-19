from sudoku_generator import SudokuGenerator
from cell import Cell
import pygame

class Board():
    def __init__(self, width, height, screen, difficulty):
        self.list_of_cells =[[0 for x in range(0,9)]for y in range(0,9)]
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.SQUARE_SIZE_VERT = int(600/3)
        self.SQUARE_SIZE_HORZ = int(600/3)
        self.LINE_COLOR_BOX = (0, 0, 0)
        self.LINE_COLOR_CELL = (242, 158, 22)
        self.LINE_COLOR_SELECT = (232, 5, 16)
        if difficulty == "easy":
            self.board = SudokuGenerator(9,30)
        if difficulty == "medium":
            self.board = SudokuGenerator(9,40)
        if difficulty == "hard":
            self.board = SudokuGenerator(9,50)
        self.board.fill_values()
        self.original_board = self.board.get_board()
        self.board.remove_cells()
        for i in range(0,9):
            for j in range(0,9):
                self.list_of_cells[i][j] = Cell(self.board.get_board()[i][j], i, j ,self.screen)
        self.selected_cell = (0,0)



    def draw(self):
        for i in range(1,9):
            pygame.draw.line(self.screen, self.LINE_COLOR_CELL, (0,i*600/9),(self.width, i*600/9),2)
        for i in range(1,9):
            pygame.draw.line(self.screen,self.LINE_COLOR_CELL,(i * 600/9,0), (600/9 * i, self.height),3)
        for i in range(0, 4):
            pygame.draw.line(self.screen, self.LINE_COLOR_BOX, (0, i * self.SQUARE_SIZE_VERT), (self.width, i * self.SQUARE_SIZE_VERT), 5)
        for i in range(0, 4):
            pygame.draw.line(self.screen, self.LINE_COLOR_BOX, (i * self.SQUARE_SIZE_HORZ,0), (self.SQUARE_SIZE_HORZ * i, self.height), 5)
        for i in range (0,9):
            for j in range(0,9):
                self.list_of_cells[i][j].draw()

        def get_list_of_cells():
            return self.list_of_cells

    def select(self, row, col):
        for i in range(0,2):
            pygame.draw.line(self.screen,self.LINE_COLOR_SELECT,(col*600/9,(row + i)*600/9),(600/9*(col+1), (row + i)*600/9),2)
        for i in range(0, 2):
            pygame.draw.line(self.screen, self.LINE_COLOR_SELECT, ((col + i) * 600 / 9, row * 600 / 9),(600/9*(col+i),(row+1)*600/9),2)
        self.selected_cell = (row,col)

    def click(self, x, y):
        if x>600 and x<0 and y>700 and y<0:
            return None
        row = 0
        col = 0
        for i in range(0,9):
            if x>=600/9*i and x<=600/9*(i+1):
                col = i
            if y >= 600 / 9 * i and y <= 600 / 9 * (i + 1):
                row=i
        result = (row,col)
        return result

    def clear(self):

        i, j = self.selected_cell
        self.list_of_cells[i][j] = Cell(0,i,j,self.screen)

    def sketch(self,value):
        i, j = self.selected_cell
        if self.original_board[i][j] >0:
            return None
        self.list_of_cells[i][j].set_sketched_value(value)
        self.list_of_cells[i][j].draw_sketched_value()

    def place_number(self,value):
        i, j = self.selected_cell
        if self.original_board[i][j] >0:
            return None
        self.list_of_cells[i][j].set_cell_value(value)
        self.list_of_cells[i][j].draw()

    def reset_to_original(self):
        for i in range(0,9):
            for j in range(0,9):
                self.list_of_cells[i][j] = self.original_board[i][j]

    def is_full(self):
        count = 0
        for i in range(0,9):
            for j in range(0,9):
                if self.list_of_cells[i][j].get_value() == 0:
                    count+=1
        if count >0:
            return False
        return True

    def update_board(self):
        for i in range(0,9):
            for j in range(0,9):
                self.board.get_board()[i][j] = self.list_of_cells[i][j].get_value()
        self.board.print_board()

    def find_empty(self):
        for i in range(0,9):
            for j in range(0,9):
                if self.list_of_cells[i][j].get_value()==0:
                    result = (i,j)
                    return result
        return None

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




