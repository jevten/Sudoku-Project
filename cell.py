from sudoku_generator import SudokuGenerator
import pygame
class Cell(SudokuGenerator):
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.board[self.row][self.col] = value

    def draw(self):
        if self.value != 0:
            font = pygame.font.SysFont('arial', 40)
            displayed_value = font.render(str(self.value),True,())