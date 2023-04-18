from sudoku_generator import SudokuGenerator
import pygame, sys
from board import Board
from cell import Cell


pygame.init()
pygame.display.set_caption("Sudoku")
screen = pygame.display.set_mode((600,700))
game_state = "start_menu"
bg_color = (193, 237, 247)

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
    print(300-medium_mode.get_width()/2-15)

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
            screen.fill(bg_color)
            board = Board(600, 600, screen, "easy")
            board.draw()


        if game_state == "medium":
            pass

        if game_state == "hard":
            pass


        pygame.display.update()