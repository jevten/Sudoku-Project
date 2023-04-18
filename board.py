from sudoku_generator import SudokuGenerator
from cell import Cell
import pygame

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.SQUARE_SIZE_VERT = int(600/3)
        self.SQUARE_SIZE_HORZ = int(600/3)
        self.LINE_COLOR_BOX = (0, 0, 0)
        self.LINE_COLOR_CELL = (242, 158, 22)

    def draw(self):
        for i in range(1,9):
            pygame.draw.line(self.screen, self.LINE_COLOR_CELL, (0,i*600/9),(self.width, i*600/9),2)
        for i in range(1,9):
            pygame.draw.line(self.screen,self.LINE_COLOR_CELL,(i * 600/9,0), (600/9 * i, self.height),3)
        for i in range(1, 4):
            pygame.draw.line(self.screen, self.LINE_COLOR_BOX, (0, i * self.SQUARE_SIZE_VERT), (self.width, i * self.SQUARE_SIZE_VERT), 5)
        for i in range(1, 3):
            pygame.draw.line(self.screen, self.LINE_COLOR_BOX, (i * self.SQUARE_SIZE_HORZ,0), (self.SQUARE_SIZE_HORZ * i, self.height), 5)
