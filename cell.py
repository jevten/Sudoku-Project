from sudoku_generator import SudokuGenerator
import pygame
class Cell(SudokuGenerator):
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.SQUARE_SIZE_VERT = int(500 / 8)
        self.SQUARE_SIZE_HORZ = int(600/8)

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.board[self.row][self.col] = value

    def draw(self):
        if self.value != 0:
            font = pygame.font.SysFont('arial', 40)
            displayed_value = font.render(str(self.value),True,())
            displayed_value_rect = displayed_value.get_rect(center=(self.col * self.SQUARE_SIZE_VERT + self.SQUARE_SIZE_VERT // 2, self.row * self.SQUARE_SIZE_HORZ + self.SQUARE_SIZE_HORZ // 2))
            self.screen.blit(displayed_value,displayed_value_rect)