from sudoku_generator import SudokuGenerator
import pygame, sys
from board import Board
from cell import Cell

#initializing pygame and declaring global variables that will be used throughout the file
pygame.init()
row,col =0,0
#creating the pygame creen
pygame.display.set_caption("Sudoku")
screen = pygame.display.set_mode((602,700))
#begin in the start menu
game_state = "start_menu"
bg_color = (193, 237, 247)
count = 0
#crete the three board for the three according difficulties
easy_board = Board(600, 600, screen, "easy")
medium_board = Board(600, 600, screen, "medium")
hard_board = Board(600, 600, screen, "hard")
font = pygame.font.SysFont('arial', 30)
reset_message = font.render("Reset", True, (242, 158, 22))



#function for displaying start menu
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

#function to display
def draw_bottom_menu():
    #create the reset messages and rectangle bheind it and displaying on bottom screen in game
    font = pygame.font.SysFont('arial', 30)
    reset_message = font.render("Reset", True, (242, 158, 22))
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(200-reset_message.get_width(),665-reset_message.get_height(),reset_message.get_width(),reset_message.get_height()))
    screen.blit(reset_message, (200 - reset_message.get_width(), 665 - reset_message.get_height()))

    #create the restart messages and rectangle bheind it and displaying on bottom screen in game
    restart_message = font.render("Restart", True,(242, 158, 22))
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(300-restart_message.get_width()//2,665-reset_message.get_height(),restart_message.get_width(),restart_message.get_height()))
    screen.blit(restart_message,(300-restart_message.get_width()//2,665-restart_message.get_height()))

    #create the exit messages and rectangle bheind it and displaying on bottom screen in game
    exit_message = font.render("Exit", True, (242, 158, 22))
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(400,665-reset_message.get_height(),exit_message.get_width(),exit_message.get_height()))
    screen.blit(exit_message,(400,665-exit_message.get_height()))

while True:
    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        #when game state is start menu
        if game_state == "start_menu":
            draw_start_menu()
            #event to select game difficulty
            if event.type == pygame.MOUSEBUTTONDOWN:
                #store the posistion of the click to decide game difficulty
                x,y = event.pos
                if x < 214.5:
                    game_state = "easy"
                elif x > 214.5 and x <435:
                    game_state = "medium"
                else:
                    game_state = "hard"

        #when game state is easy sudoku
        if game_state == "easy":
            if count == 0:
                x,y = 0,0
                #draw easy screen
                screen.fill(bg_color)
                easy_board.draw()
                draw_bottom_menu()
                count += 1

            #implement the use of the arrow keys to select cells to change
            if event.type == pygame.KEYDOWN:
                easy_board.draw()
                #increase column selection when right key is pressed
                if event.key == pygame.K_RIGHT and col<8:
                    col+=1
                    easy_board.select(row, col)
                #decrease column selection when left key is pressed
                if event.key == pygame.K_LEFT and col > 0:
                    col-=1
                    easy_board.select(row,col)
                #decrease the row selection when up key is pressed
                if event.key == pygame.K_UP and row > 0:
                    row -= 1
                    easy_board.select(row, col)
                #increase the row selection when the down key is pressed
                if event.key == pygame.K_DOWN and row < 8:
                    row += 1
                    easy_board.select(row, col)

            #event action when the mouse is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                easy_board.draw()
                #store the location of the click to determine posistion on board
                x,y = event.pos
                #if the click is in the bottom menu instead of sudoku game
                if y>600:
                    #reset the board to original state without changed cells
                    if x<200:
                        for i in range(0,9):
                            for j in range(0,9):
                                easy_board.list_of_cells[i][j].set_cell_value(easy_board.original_board[i][j])
                        screen.fill(bg_color)
                        easy_board.draw()
                        draw_bottom_menu()
                    #restart by sending the user back to the start menu
                    if x>200 and x<400:
                        game_state = "start_menu"
                        count = 0
                    #exit the function selection
                    if x>400:
                        pygame.quit()
                        sys.exit()
                #determine the row and col of the click to make cell selection
                row, col = easy_board.click(x,y)
                x,y = row*600/9, col*600/9
                #use class method to select a cell
                easy_board.select(row,col)
            #event when the user types in a value for the selected cell
            if event.type == pygame.KEYDOWN:
                #ensure the user can only change values that were not given
                if easy_board.original_board[row][col]==0:
                    #sketch the 1 when it is entered
                    if event.key == pygame.K_1:
                        pygame.draw.rect(screen,(193, 237, 247), pygame.Rect(col*600/9+2,row*600/9+2,600/9-4,600/9-4))
                        easy_board.clear()
                        easy_board.sketch(1)
                    #sketch the 2 when it is entered
                    if event.key == pygame.K_2:
                        pygame.draw.rect(screen, (193, 237, 247),pygame.Rect(col * 600 / 9 + 2, row * 600 / 9 + 2, 600 / 9-4, 600 / 9-4))
                        easy_board.clear()
                        easy_board.sketch(2)
                    #sketch the 3 when it is entered
                    if event.key == pygame.K_3:
                        pygame.draw.rect(screen, (193, 237, 247),pygame.Rect(col * 600 / 9 + 2, row * 600 / 9 + 2, 600 / 9 - 4, 600 / 9 - 4))
                        easy_board.clear()
                        easy_board.sketch(3)
                    #sketch the 4 when it is entered
                    if event.key == pygame.K_4:
                        pygame.draw.rect(screen, (193, 237, 247),pygame.Rect(col * 600 / 9 + 2, row * 600 / 9 + 2, 600 / 9 - 4, 600 / 9 - 4))
                        easy_board.clear()
                        easy_board.sketch(4)
                    #sketch the 5 when it is entered
                    if event.key == pygame.K_5:
                        pygame.draw.rect(screen, (193, 237, 247),pygame.Rect(col * 600 / 9 + 2, row * 600 / 9 + 2, 600 / 9 - 4, 600 / 9 - 4))
                        easy_board.clear()
                        easy_board.sketch(5)
                    #sketch the 6 when it is entered
                    if event.key == pygame.K_6:
                        pygame.draw.rect(screen, (193, 237, 247),pygame.Rect(col * 600 / 9 + 2, row * 600 / 9 + 2, 600 / 9 - 4, 600 / 9 - 4))
                        easy_board.clear()
                        easy_board.sketch(6)
                    #sketch the 7 when it is entered
                    if event.key == pygame.K_7:
                        pygame.draw.rect(screen, (193, 237, 247),pygame.Rect(col * 600 / 9 + 2, row * 600 / 9 + 2, 600 / 9 - 4, 600 / 9 - 4))
                        easy_board.clear()
                        easy_board.sketch(7)
                    #sketch the 8 when it is entered
                    if event.key == pygame.K_8:
                        pygame.draw.rect(screen, (193, 237, 247),pygame.Rect(col * 600 / 9 + 2, row * 600 / 9 + 2, 600 / 9 - 4, 600 / 9 - 4))
                        easy_board.clear()
                        easy_board.sketch(8)
                    #sketch the 9 when it is entered
                    if event.key == pygame.K_9:
                        pygame.draw.rect(screen, (193, 237, 247),pygame.Rect(col * 600 / 9 + 2, row * 600 / 9 + 2, 600 / 9 - 4, 600 / 9 - 4))
                        easy_board.clear()
                        easy_board.sketch(9)
                    #reset the cell value when 0 is entered
                    if event.key == pygame.K_0:
                        pygame.draw.rect(screen, (193, 237, 247),pygame.Rect(col * 600 / 9 + 2, row * 600 / 9 + 2, 600 / 9 - 4, 600 / 9 - 4))
                        easy_board.clear()
                    #when the user presses return or enter, the value is locked in and no longer sketched
                    if event.key == pygame.K_RETURN:
                        easy_board.list_of_cells[row][col].set_cell_value(easy_board.list_of_cells[row][col].get_sketched_Value())
                        pygame.draw.rect(screen, (193, 237, 247),pygame.Rect(col * 600 / 9 + 2, row * 600 / 9 + 2, 600 / 9 - 4, 600 / 9 - 4))
                        easy_board.list_of_cells[row][col].draw()
            #check if all values on the board are entered
            if easy_board.is_full():
               easy_board.update_board()
               #check if the user correctly or incorrectly enter the values to check if they won or lost
               if easy_board.check_board():
                   game_state = "win"
               else:
                   game_state = "lose"


            pygame.display.update()


        #when game state is in medium difficulty mode
        if game_state == "medium":
            if count == 0:
                #draw the medium board
                screen.fill(bg_color)
                medium_board.draw()
                draw_bottom_menu()
                count += 1
            #action when the mouse is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                medium_board.draw()
                #stoe posistion of the click
                x,y = event.pos
                #when the user clicks something in the bottom menu
                if y>600:
                    #user selects to reset the board to the original state
                    if x<200:
                        for i in range(0,9):
                            for j in range(0,9):
                                medium_board.list_of_cells[i][j].set_cell_value(medium_board.original_board[i][j])
                        screen.fill(bg_color)
                        medium_board.draw()
                        draw_bottom_menu()
                    #when the user selects to restart send them back to the  main menu
                    if x>200 and x<400:
                        game_state = "start_menu"
                        count = 0
                    #user selcts to quit so quit
                    if x>400:
                        pygame.quit()
                        sys.exit()
                #use class methods to store the row and col value of the click and select the cell
                row, col = medium_board.click(x,y)
                medium_board.select(row,col)

            # implmentation of using the arrow keys to select cells
            if event.type == pygame.KEYDOWN:
                medium_board.draw()
                #increase col when right is entered
                if event.key == pygame.K_RIGHT and col<8:
                    col+=1
                    medium_board.select(row, col)
                #decrease col when left is entered
                if event.key == pygame.K_LEFT and col > 0:
                    col-=1
                    medium_board.select(row,col)
                #decrease row when up is entered
                if event.key == pygame.K_UP and row > 0:
                    row -= 1
                    medium_board.select(row, col)
                #increase row when down is entered
                if event.key == pygame.K_DOWN and row < 8:
                    row += 1
                    medium_board.select(row, col)

            #event when the user enters a value into selected cell
            if event.type == pygame.KEYDOWN:
                #ensure the user cant change values given to them
                if medium_board.original_board[row][col]==0:
                    #sketch the 1 when it is entered
                    if event.key == pygame.K_1:
                        pygame.draw.rect(screen,(193, 237, 247), pygame.Rect(col*600/9+2,row*600/9+2,600/9-4,600/9-4))
                        medium_board.clear()
                        medium_board.sketch(1)
                    # sketch the 2 when it is entered
                    if event.key == pygame.K_2:
                        pygame.draw.rect(screen, (193, 237, 247),pygame.Rect(col * 600 / 9 + 2, row * 600 / 9 + 2, 600 / 9-4, 600 / 9-4))
                        medium_board.clear()
                        medium_board.sketch(2)
                    # sketch the 3 when it is entered
                    if event.key == pygame.K_3:
                        pygame.draw.rect(screen, (193, 237, 247),pygame.Rect(col * 600 / 9 + 2, row * 600 / 9 + 2, 600 / 9 - 4, 600 / 9 - 4))
                        medium_board.clear()
                        medium_board.sketch(3)
                    # sketch the 4 when it is entered
                    if event.key == pygame.K_4:
                        pygame.draw.rect(screen, (193, 237, 247),pygame.Rect(col * 600 / 9 + 2, row * 600 / 9 + 2, 600 / 9 - 4, 600 / 9 - 4))
                        medium_board.clear()
                        medium_board.sketch(4)
                    # sketch the 5 when it is entered
                    if event.key == pygame.K_5:
                        pygame.draw.rect(screen, (193, 237, 247),pygame.Rect(col * 600 / 9 + 2, row * 600 / 9 + 2, 600 / 9 - 4, 600 / 9 - 4))
                        medium_board.clear()
                        medium_board.sketch(5)
                    # sketch the 6 when it is entered
                    if event.key == pygame.K_6:
                        pygame.draw.rect(screen, (193, 237, 247),pygame.Rect(col * 600 / 9 + 2, row * 600 / 9 + 2, 600 / 9 - 4, 600 / 9 - 4))
                        medium_board.clear()
                        medium_board.sketch(6)
                    # sketch the 7 when it is entered
                    if event.key == pygame.K_7:
                        pygame.draw.rect(screen, (193, 237, 247),pygame.Rect(col * 600 / 9 + 2, row * 600 / 9 + 2, 600 / 9 - 4, 600 / 9 - 4))
                        medium_board.clear()
                        medium_board.sketch(7)
                    # sketch the 8 when it is entered
                    if event.key == pygame.K_8:
                        pygame.draw.rect(screen, (193, 237, 247),pygame.Rect(col * 600 / 9 + 2, row * 600 / 9 + 2, 600 / 9 - 4, 600 / 9 - 4))
                        medium_board.clear()
                        medium_board.sketch(8)
                    # sketch the 9 when it is entered
                    if event.key == pygame.K_9:
                        pygame.draw.rect(screen, (193, 237, 247),pygame.Rect(col * 600 / 9 + 2, row * 600 / 9 + 2, 600 / 9 - 4, 600 / 9 - 4))
                        medium_board.clear()
                        medium_board.sketch(9)
                    # reset the value the user entered or sketched by entering 0
                    if event.key == pygame.K_0:
                        pygame.draw.rect(screen, (193, 237, 247),pygame.Rect(col * 600 / 9 + 2, row * 600 / 9 + 2, 600 / 9 - 4, 600 / 9 - 4))
                        medium_board.clear()
                    # set the real value of the cell to the sketched value when the user hit enter/return
                    if event.key == pygame.K_RETURN:
                        medium_board.list_of_cells[row][col].set_cell_value(medium_board.list_of_cells[row][col].get_sketched_Value())
                        pygame.draw.rect(screen, (193, 237, 247),pygame.Rect(col * 600 / 9 + 2, row * 600 / 9 + 2, 600 / 9 - 4, 600 / 9 - 4))
                        medium_board.list_of_cells[row][col].draw()
            #cuses call method to check if the board is full and game is over
            if medium_board.is_full():
                medium_board.update_board()
                #use class method to determine if game is won or lost
                if medium_board.check_board():
                    game_state = "win"
                else:
                    game_state = "lose"

        #handler for when game state is in hard
        if game_state == "hard":
            if count == 0:
                #draw the hard board
                screen.fill(bg_color)
                hard_board.draw()
                draw_bottom_menu()
                count += 1
            #even the a user clicks
            if event.type == pygame.MOUSEBUTTONDOWN:
                hard_board.draw()
                #store the location of the click
                x,y = event.pos
                #if the user clicks the bottom menu
                if y>600:
                    #when the user selects the reset button, reset the board to original board
                    if x<200:
                        for i in range(0,9):
                            for j in range(0,9):
                                hard_board.list_of_cells[i][j].set_cell_value(hard_board.original_board[i][j])
                        screen.fill(bg_color)
                        hard_board.draw()
                        draw_bottom_menu()
                    #when the user selects restart send them back to start menu
                    if x>200 and x<400:
                        game_state = "start_menu"
                        count = 0
                    #when the user selects to quit, quit pygame and system
                    if x>400:
                        pygame.quit()
                        sys.exit()
                #use class method to create row and col values based on the location of the clik
                row, col = hard_board.click(x,y)
                #select to clicked location using class method
                hard_board.select(row,col)

            #when the user presses a key
            if event.type == pygame.KEYDOWN:
                hard_board.draw()
                #implementation of using the arrow keys to select a cell
                #increase col when right is entered
                if event.key == pygame.K_RIGHT and col<8:
                    col+=1
                    hard_board.select(row, col)
                #decrease col when left is entered
                if event.key == pygame.K_LEFT and col > 0:
                    col-=1
                    hard_board.select(row,col)
                #decrease row when up is selected
                if event.key == pygame.K_UP and row > 0:
                    row -= 1
                    hard_board.select(row, col)
                #increase row when down is selected
                if event.key == pygame.K_DOWN and row < 8:
                    row += 1
                    hard_board.select(row, col)

            #when a user enters a value
            if event.type == pygame.KEYDOWN:
                #ensure the user can't change given values
                if hard_board.original_board[row][col]==0:
                    # sketch the 1 when it is entered
                    if event.key == pygame.K_1:
                        pygame.draw.rect(screen,(193, 237, 247), pygame.Rect(col*600/9+2,row*600/9+2,600/9-4,600/9-4))
                        hard_board.clear()
                        hard_board.sketch(1)
                    # sketch the 2 when it is entered
                    if event.key == pygame.K_2:
                        pygame.draw.rect(screen, (193, 237, 247),pygame.Rect(col * 600 / 9 + 2, row * 600 / 9 + 2, 600 / 9-4, 600 / 9-4))
                        hard_board.clear()
                        hard_board.sketch(2)
                    # sketch the 3 when it is entered
                    if event.key == pygame.K_3:
                        pygame.draw.rect(screen, (193, 237, 247),pygame.Rect(col * 600 / 9 + 2, row * 600 / 9 + 2, 600 / 9 - 4, 600 / 9 - 4))
                        hard_board.clear()
                        hard_board.sketch(3)
                    # sketch the 4 when it is entered
                    if event.key == pygame.K_4:
                        pygame.draw.rect(screen, (193, 237, 247),pygame.Rect(col * 600 / 9 + 2, row * 600 / 9 + 2, 600 / 9 - 4, 600 / 9 - 4))
                        hard_board.clear()
                        hard_board.sketch(4)
                    # sketch the 5 when it is entered
                    if event.key == pygame.K_5:
                        pygame.draw.rect(screen, (193, 237, 247),pygame.Rect(col * 600 / 9 + 2, row * 600 / 9 + 2, 600 / 9 - 4, 600 / 9 - 4))
                        hard_board.clear()
                        hard_board.sketch(5)
                    # sketch the 6 when it is entered
                    if event.key == pygame.K_6:
                        pygame.draw.rect(screen, (193, 237, 247),pygame.Rect(col * 600 / 9 + 2, row * 600 / 9 + 2, 600 / 9 - 4, 600 / 9 - 4))
                        hard_board.clear()
                        hard_board.sketch(6)
                    # sketch the 7 when it is entered
                    if event.key == pygame.K_7:
                        pygame.draw.rect(screen, (193, 237, 247),pygame.Rect(col * 600 / 9 + 2, row * 600 / 9 + 2, 600 / 9 - 4, 600 / 9 - 4))
                        hard_board.clear()
                        hard_board.sketch(7)
                    # sketch the 8 when it is entered
                    if event.key == pygame.K_8:
                        pygame.draw.rect(screen, (193, 237, 247),pygame.Rect(col * 600 / 9 + 2, row * 600 / 9 + 2, 600 / 9 - 4, 600 / 9 - 4))
                        hard_board.clear()
                        hard_board.sketch(8)
                    # sketch the 9 when it is entered
                    if event.key == pygame.K_9:
                        pygame.draw.rect(screen, (193, 237, 247),pygame.Rect(col * 600 / 9 + 2, row * 600 / 9 + 2, 600 / 9 - 4, 600 / 9 - 4))
                        hard_board.clear()
                        hard_board.sketch(9)
                    #when the user enters 0 reset the cell value
                    if event.key == pygame.K_0:
                        pygame.draw.rect(screen, (193, 237, 247),pygame.Rect(col * 600 / 9 + 2, row * 600 / 9 + 2, 600 / 9 - 4, 600 / 9 - 4))
                        hard_board.clear()
                    #when the user presses enter change the cells value to the sektched value
                    if event.key == pygame.K_RETURN:
                        hard_board.list_of_cells[row][col].set_cell_value(hard_board.list_of_cells[row][col].get_sketched_Value())
                        pygame.draw.rect(screen, (193, 237, 247),pygame.Rect(col * 600 / 9 + 2, row * 600 / 9 + 2, 600 / 9 - 4, 600 / 9 - 4))
                        hard_board.list_of_cells[row][col].draw()
            #use class method to check if the board is full
            if hard_board.is_full():
                # us class method the check is board is solved correctly to send to win or lose screen
               hard_board.update_board()
               if hard_board.check_board():
                   game_state = "win"
               else:
                   game_state = "lose"

        #when a user loses, display this lose screen
        if game_state == "lose":
            bg_img = pygame.image.load("sudokupic.webp")
            screen.fill((0, 0, 0))
            # display background image
            screen.blit(bg_img, (0, 0))
            #message on screen creation
            lose_font = pygame.font.SysFont('arial', 70)
            lose_message = lose_font.render('Game Over :(', True, (0, 0, 0))
            #blit the losing message on screen
            screen.blit(lose_message,(300 - lose_message.get_width()/2, 300 - lose_message.get_height()))
            #create restart message
            restart_message = lose_font.render("Restart", True, (242, 158, 22))
            #draw background rectangle behind restart option
            pygame.draw.rect(screen, (0, 0, 0),pygame.Rect(300 - restart_message.get_width() // 2, 500 - reset_message.get_height(), restart_message.get_width(), restart_message.get_height()))
            #blit restart message on rectangle
            screen.blit(restart_message,(300-restart_message.get_width()/2,500-restart_message.get_height()/2))
            #when the user presses the restart option, restart the board like in the bottom menu
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(0, 9):
                    for j in range(0, 9):
                        easy_board.list_of_cells[i][j].set_cell_value(easy_board.original_board[i][j])
                        medium_board.list_of_cells[i][j].set_cell_value(medium_board.original_board[i][j])
                        hard_board.list_of_cells[i][j].set_cell_value(hard_board.original_board[i][j])
                game_state = "start_menu"
                count = 0
        #when a user wins, display the win screen
        if game_state == "win":
            bg_img = pygame.image.load("sudokupic.webp")
            screen.fill((0, 0, 0))
            # display background image
            screen.blit(bg_img, (0, 0))
            #create game winnign message
            lose_font = pygame.font.SysFont('arial', 70)
            #blit game win message
            lose_message = lose_font.render('Game Won!', True, (0, 0, 0))
            screen.blit(lose_message, (300 - lose_message.get_width() / 2, 300 - lose_message.get_height()))
            #create exit mesaage
            restart_message = lose_font.render("Exit", True, (242, 158, 22))
            #draw bg rectangle for exit message
            pygame.draw.rect(screen, (0, 0, 0),pygame.Rect(300 - restart_message.get_width() // 2, 500 - reset_message.get_height(),restart_message.get_width(), restart_message.get_height()))
            #blit the exit message over the rectange
            screen.blit(restart_message,(300 - restart_message.get_width() / 2, 500 - restart_message.get_height() / 2))
            #when the user selects the exit option, exit the program
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()
                sys.exit()
        pygame.display.update()