from sudoku_generator import SudokuGenerator
import pygame
class Cell(SudokuGenerator):
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.CELL_SIZE_VERT = 600/9
        self.CELL_SIZE_HORZ = 600/9

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.board[self.row][self.col] = value

    def draw(self):
        if self.value != 0:
            font = pygame.font.SysFont('arial', 40)
            displayed_value = font.render(str(self.value),True,(242, 158, 22))
            displayed_value_rect = displayed_value.get_rect(center=(self.col * self.CELL_SIZE_VERT + self.CELL_SIZE_VERT // 2, self.row * self.CELL_SIZE_HORZ + self.CELL_SIZE_HORZ // 2))
            self.screen.blit(displayed_value,displayed_value_rect)