from sudoku_generator import SudokuGenerator
import pygame

class Cell:
    #constructor for cell class
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        #size of each cell based on the board size 600x600
        self.CELL_SIZE_VERT = 600/9
        self.CELL_SIZE_HORZ = 600/9
        self.sketched_value= 0

    #function to change the value of the cell
    def set_cell_value(self, value):
        self.value = value

    #function to change the sketched value of the cell
    def set_sketched_value(self, value):
        self.sketched_value = value

    #function to return the value of the cell
    def get_value(self):
        return self.value

    #fucntion to return the sketched value of the functoin
    def get_sketched_Value(self):
        return self.sketched_value

    #draw the entered value of the cell
    def draw(self):
        #only draw whn value is not zero
        if self.value != 0:
            #create value message on screen
            font = pygame.font.SysFont('arial', 40)
            displayed_value = font.render(str(self.value),True,(242, 158, 22))
            #center the value in the cell
            displayed_value_rect = displayed_value.get_rect(center=(self.col * self.CELL_SIZE_VERT + self.CELL_SIZE_VERT // 2, self.row * self.CELL_SIZE_HORZ + self.CELL_SIZE_HORZ // 2))
            #blit the value on screen
            self.screen.blit(displayed_value,displayed_value_rect)

    #function to draw the sketched value of the cell on screen
    def draw_sketched_value(self):
        #create sketched value message
        font = pygame.font.SysFont('arial', 20)
        displayed_sketch_value = font.render(str(self.sketched_value),True,(66, 64, 64))
        #create the loctation of the message to be in upper left of the cell
        displayed_value_rect = displayed_sketch_value.get_rect(center=(self.col * self.CELL_SIZE_VERT+self.CELL_SIZE_VERT//5,self.row * self.CELL_SIZE_HORZ+self.CELL_SIZE_HORZ//4))
        #blit the value on the screen
        self.screen.blit(displayed_sketch_value, displayed_value_rect)

