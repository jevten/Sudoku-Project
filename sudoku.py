from sudoku_generator import SudokuGenerator
import pygame, sys

pygame.init()
pygame.display.set_caption("Sudoku")
screen = pygame.display.set_mode((600,600))
game_state = "start_menu"

def draw_start_menu():
    bg_img = pygame.image.load("sudokupic.webp")
    screen.fill((0,0,0))
    screen.blit(bg_img,(0,0))
    font = pygame.font.SysFont('arial', 40)
    title = font.render('Welcome to Sudoku', True, (242, 158, 22))
    message = font.render("Select Game Mode", True, (242, 158, 22))
    easy_mode = font.render('Easy', True, (242, 158, 22))
    medium_mode = font.render("Medium", True, (242, 158, 22))
    hard_mode = font.render("Hard", True, (242, 158, 22))
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(300-medium_mode.get_width()/2-15, 500, medium_mode.get_width() + 30, easy_mode.get_height() + 30))
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(50, 500, easy_mode.get_width() + 30 , easy_mode.get_height() + 30))
    pygame.draw.rect(screen,(0,0,0), pygame.Rect(435,500, hard_mode.get_width()+30, easy_mode.get_height()+30))
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

        pygame.display.update()