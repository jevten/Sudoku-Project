from sudoku_generator import SudokuGenerator
import pygame, sys
from board import Board
from cell import Cell


pygame.init()
pygame.display.set_caption("Sudoku")
screen = pygame.display.set_mode((602,700))
game_state = "start_menu"
bg_color = (193, 237, 247)
count = 0
easy_board = Board(600, 600, screen, "easy")

def draw_start_menu():
    #load background image
    bg_img = pygame.image.load("sudokupic.webp")
    screen.fill((0,0,0))
    #display background image
    screen.blit(bg_img,(0,0))
    font = pygame.font.SysFont('arial', 40)
    #render the text for start srceens
    title = font.render('Welcome to Sudoku', True, (242, 158, 22))
    message = font.render("Select Game Mode", True, (242, 158, 22))
    easy_mode = font.render('Easy', True, (242, 158, 22))
    medium_mode = font.render("Medium", True, (242, 158, 22))
    hard_mode = font.render("Hard", True, (242, 158, 22))
    #create rectangles and screen for game options to be over layed to
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(300-medium_mode.get_width()/2-15, 500, medium_mode.get_width() + 30, easy_mode.get_height() + 30))
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(50, 500, easy_mode.get_width() + 30 , easy_mode.get_height() + 30))
    pygame.draw.rect(screen,(0,0,0), pygame.Rect(435,500, hard_mode.get_width()+30, easy_mode.get_height()+30))
    #print the messages on the screen
    screen.blit(hard_mode, (450, 515))
    screen.blit(medium_mode, (300-medium_mode.get_width()/2, 515))
    screen.blit(message,(300 - message.get_width()/2, 300 - message.get_height()))
    screen.blit(title, (600/2 - title.get_width() / 2, 175- title.get_height()))
    screen.blit(easy_mode, (65, 515))
    pygame.display.update()

while True:
    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if game_state == "start_menu":
            draw_start_menu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = event.pos
                if x < 214.5:
                    game_state = "easy"
                elif x > 214.5 and x <435:
                    game_state = "medium"
                else:
                    game_state = "hard"

        if game_state == "easy":
            if count == 0:
                screen.fill(bg_color)
                easy_board.draw()
                count += 1
            if event.type == pygame.MOUSEBUTTONDOWN:
                easy_board.draw()
                x,y = event.pos
                row, col = easy_board.click(x,y)
                easy_board.select(row,col)
            if event.type == pygame.KEYDOWN:
                if easy_board.original_board[row][col]==0:
                    if event.key == pygame.K_1:
                        pygame.draw.rect(screen,(193, 237, 247), pygame.Rect(col*600/9+2,row*600/9+2,600/9-4,600/9-4))
                        easy_board.clear()
                        easy_board.sketch(1)
                    if event.key == pygame.K_2:
                        pygame.draw.rect(screen, (193, 237, 247),pygame.Rect(col * 600 / 9 + 2, row * 600 / 9 + 2, 600 / 9-4, 600 / 9-4))
                        easy_board.clear()
                        easy_board.sketch(2)
                    if event.key == pygame.K_3:
                        pygame.draw.rect(screen, (193, 237, 247),pygame.Rect(col * 600 / 9 + 2, row * 600 / 9 + 2, 600 / 9 - 4, 600 / 9 - 4))
                        easy_board.clear()
                        easy_board.sketch(3)
                    if event.key == pygame.K_4:
                        pygame.draw.rect(screen, (193, 237, 247),pygame.Rect(col * 600 / 9 + 2, row * 600 / 9 + 2, 600 / 9 - 4, 600 / 9 - 4))
                        easy_board.clear()
                        easy_board.sketch(4)
                    if event.key == pygame.K_5:
                        pygame.draw.rect(screen, (193, 237, 247),pygame.Rect(col * 600 / 9 + 2, row * 600 / 9 + 2, 600 / 9 - 4, 600 / 9 - 4))
                        easy_board.clear()
                        easy_board.sketch(5)
                    if event.key == pygame.K_6:
                        pygame.draw.rect(screen, (193, 237, 247),pygame.Rect(col * 600 / 9 + 2, row * 600 / 9 + 2, 600 / 9 - 4, 600 / 9 - 4))
                        easy_board.clear()
                        easy_board.sketch(6)
                    if event.key == pygame.K_7:
                        pygame.draw.rect(screen, (193, 237, 247),pygame.Rect(col * 600 / 9 + 2, row * 600 / 9 + 2, 600 / 9 - 4, 600 / 9 - 4))
                        easy_board.clear()
                        easy_board.sketch(7)
                    if event.key == pygame.K_8:
                        pygame.draw.rect(screen, (193, 237, 247),pygame.Rect(col * 600 / 9 + 2, row * 600 / 9 + 2, 600 / 9 - 4, 600 / 9 - 4))
                        easy_board.clear()
                        easy_board.sketch(8)
                    if event.key == pygame.K_9:
                        pygame.draw.rect(screen, (193, 237, 247),pygame.Rect(col * 600 / 9 + 2, row * 600 / 9 + 2, 600 / 9 - 4, 600 / 9 - 4))
                        easy_board.clear()
                        easy_board.sketch(9)
                    if event.key == pygame.K_0:
                        pygame.draw.rect(screen, (193, 237, 247),pygame.Rect(col * 600 / 9 + 2, row * 600 / 9 + 2, 600 / 9 - 4, 600 / 9 - 4))
                        easy_board.clear()
                    if event.key == pygame.K_RETURN:
                        easy_board.list_of_cells[row][col].set_cell_value(easy_board.list_of_cells[row][col].get_sketched_Value())
                        pygame.draw.rect(screen, (193, 237, 247),pygame.Rect(col * 600 / 9 + 2, row * 600 / 9 + 2, 600 / 9 - 4, 600 / 9 - 4))
                        easy_board.list_of_cells[row][col].draw()
            pygame.display.update()



        if game_state == "medium":
            pass

        if game_state == "hard":
            pass


        pygame.display.update()