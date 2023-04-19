from sudoku_generator import SudokuGenerator
from cell import Cell
import pygame

class Board:
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
        self.board.remove_cells()
        for i in range(0,9):
            for j in range(0,9):
                self.list_of_cells[i][j] = Cell(self.board.get_board()[i][j], i, j ,self.screen)



    def draw(self):
        for i in range(1,9):
            pygame.draw.line(self.screen, self.LINE_COLOR_CELL, (0,i*600/9),(self.width, i*600/9),2)
        for i in range(1,9):
            pygame.draw.line(self.screen,self.LINE_COLOR_CELL,(i * 600/9,0), (600/9 * i, self.height),3)
        for i in range(1, 4):
            pygame.draw.line(self.screen, self.LINE_COLOR_BOX, (0, i * self.SQUARE_SIZE_VERT), (self.width, i * self.SQUARE_SIZE_VERT), 5)
        for i in range(1, 3):
            pygame.draw.line(self.screen, self.LINE_COLOR_BOX, (i * self.SQUARE_SIZE_HORZ,0), (self.SQUARE_SIZE_HORZ * i, self.height), 5)
        for i in range (0,9):
            for j in range(0,9):
                self.list_of_cells[i][j].draw()

    def select(self,row,col):
        for i in range(0,2):
            pygame.draw.line(self.screen,self.LINE_COLOR_SELECT,(col*600/9,(row + i)*600/9),(600/9*(col+1), (row + i)*600/9),5)
        for i in range(0, 2):
            pygame.draw.line(self.screen, self.LINE_COLOR_SELECT, ((col + i) * 600 / 9, row * 600 / 9),(600/9*(col+i),(row+1)*600/9),5)

    def click(self, x, y):
        if x>600 and x<0 and y>600 and y<0:
            return None
        row = 0
        col = 0
        for i in range(0,9):
            if x>=600/9*i and x<=600/9*(i+1):
                col = i
            if y >= 600 / 9 * i and y <= 600 / 9 * (i + 1):
                y=i
        result = (row,col)
        return result

