import pygame
import random
import pygame, sys
from pygame.locals import *
 
pygame.init()
 
screen = pygame.display.set_mode((1500, 1000))


# importing the Scroller to use as background

#from scroller2 import Scroller as Scroller
    

BLACK = (0, 0, 0)

WHITE = (255, 255, 255)

RED = (255, 0, 0)

GREEN = (0, 255, 0)

BLUE = (255, 0, 0)


class Block(pygame.sprite.Sprite):


    def __init__(self, file_name):

        super().__init__()

        # Loading the sprite from the file

        self.image = pygame.image.load(file_name)

        # This sets the background of the image.

        # Setting it to white makes it so that it blends in the rest of screen

        self.image.set_colorkey(WHITE)

        self.rect = self.image.get_rect()



    def update(self):

        self.rect.x -= 1

##        if self.rect.x < 0:
##            #self.rect.y = random.randrange(0, screen_height)'
##            if self in up_notes:
##                self.rect.y = screen_height//4
##            elif self in down_notes:
##                self.rect.y = screen_height//2
##            else:
##                self.rect.x = screen_width + 10
##                self.rect.y = random.randrange(0, screen_height)



pygame.init()

screen_width = 1000

screen_height = 700

screen = pygame.display.set_mode([screen_width, screen_height])

bad_sprites_list = pygame.sprite.Group()


good_sprites_list = pygame.sprite.Group()


all_sprites_list = pygame.sprite.Group()

player = Block("girl.png")
player.rect.x=400
player.rect.y=400

# This makes the 


def make_sprites(level):

    '''

    This makes the sprites.

    The level argument is used to decide how many bad sprites there are

    '''

    all_sprites_list.add(player)

    a1 = Block("A-note.png")
    a2 = Block("A-note.png")
    a3 = Block("A-note.png")
    a4 = Block("A-note.png")
    a5 = Block("A-note.png")
    a6 = Block("A-note.png")
    
    b1 = Block("B-note.png")
    b2 = Block("B-note.png")
    b3 = Block("B-note.png")
    b4 = Block("B-note.png")
    b5 = Block("B-note.png")
    b6 = Block("B-note.png")

    c1 = Block("C-note.png")
    c2 = Block("C-note.png")
    c3 = Block("C-note.png")
    c4 = Block("C-note.png")
    c5 = Block("C-note.png")
    c6 = Block("C-note.png")
    c7 = Block("C-note.png")
    c8 = Block("C-note.png")
    c9 = Block("C-note.png")
    c10 = Block("C-note.png")   
    c11 = Block("C-note.png")
    c12 = Block("C-note.png")
    
    d1 = Block("D-note.png")
    d2 = Block("D-note.png")
    d2 = Block("D-note.png")
    d3 = Block("D-note.png")
    d4 = Block("D-note.png")
    d5 = Block("D-note.png")
    d6 = Block("D-note.png")
    d7 = Block("D-note.png")
    d8 = Block("D-note.png")
    d9 = Block("D-note.png")
    d10 = Block("D-note.png")
    d11 = Block("D-note.png")
    d12 = Block("D-note.png")
    d13 = Block("D-note.png")
    d14 = Block("D-note.png")
    d15 = Block("D-note.png")
    d16 = Block("D-note.png")
    d17 = Block("D-note.png")
    d18 = Block("D-note.png")
    d19 = Block("D-note.png")
    d20 = Block("D-note.png")
    d21 = Block("D-note.png")
    d22 = Block("D-note.png")
    d23 = Block("D-note.png")
    d24 = Block("D-note.png")
    d25 = Block("D-note.png")
    d26 = Block("D-note.png")
    d27 = Block("D-note.png")
    d28 = Block("D-note.png")
    d29 = Block("D-note.png")
    d30 = Block("D-note.png")
    
    
    e1 = Block("E-note.png")
    e2 = Block("E-note.png")
    e3 = Block("E-note.png")
    e4 = Block("E-note.png")
    e5 = Block("E-note.png")
    e6 = Block("E-note.png")
    e7 = Block("E-note.png")
    e8 = Block("E-note.png")
    e9 = Block("E-note.png")
    e10 = Block("E-note.png")
    e11 = Block("E-note.png")
    e12 = Block("E-note.png")
    e13 = Block("E-note.png")
    e14 = Block("E-note.png")
    e15 = Block("E-note.png")
    e16 = Block("E-note.png")
    e17 = Block("E-note.png")
    e18 = Block("E-note.png")
    e19 = Block("E-note.png")
    e20 = Block("E-note.png")
    e21 = Block("E-note.png")
    e22 = Block("E-note.png")
    e23 = Block("E-note.png")
    e24 = Block("E-note.png")
    e25 = Block("E-note.png")
    e26 = Block("E-note.png")
    e27 = Block("E-note.png")
    e28 = Block("E-note.png")
    e29 = Block("E-note.png")
    e30 = Block("E-note.png")
    e31 = Block("E-note.png")
    e32 = Block("E-note.png")
    e33 = Block("E-note.png")
    e34 = Block("E-note.png")
    
    f1 = Block("F-note.png")
    f2 = Block("F-note.png")
    f3 = Block("F-note.png")
    f4 = Block("F-note.png")
    f5 = Block("F-note.png")
    f6 = Block("F-note.png")
    f7 = Block("F-note.png")
    f8 = Block("F-note.png")
    f9 = Block("F-note.png")
    f10 = Block("F-note.png")
    
    g1 = Block("G-note.png")
    g2 = Block("G-note.png")
    g3 = Block("G-note.png")
    g4 = Block("G-note.png")
    g5 = Block("G-note.png")
    g6 = Block("G-note.png")
    g7 = Block("G-note.png")
    g8 = Block("G-note.png")

    up_notes = [e1, d1, f1, d2, d3, b1, e2, a1, d4, d5, e3, e4, e5, e6, e7, c1, c2, e8, f2, f3, f4, d6, f5, d7, d8, b2, c3, e9, e10, c4, e11, e12, d9, e13, d10, e14, d11, e15, f6, g1, e16, a2, d12, d13, e17, f7, e18, e19, e20, e21, a3, b3, g2]

    down_notes = [a4, c5, c6, g3, e22, e23, g4, d14, a5, c7, g5, g6, g7, d15, d16, b4, d17, a6, e24, e25, e26, e27, d18, e28, c8, c9, d19, d20, d21, b5, d22, d23, e29, d24, e30, d25, e31, d26, g8, f8, b6, d27, c10, e32, f9, e33, c11, f10, d28, d29, e34, d30, c12]

    good_notes = [e1, d1, c6, d2, e22, e23, e2, d14, d4, d5, e3, g6, g7, e6, d16, c1, d17, e8, e24, e25, e26, d6, d18, e28, d8, c9, d19, e9, d21, c4, d22, e12, e29, e13, d10, d25, d11, e15, g8, g1, e16, d27, c10, d13, e17, e33, e18, e19, d28, d29, e34, d30, c12]
    my_x = 200
    d_x = 125
    
    for i in up_notes:
        i.rect.x = my_x
        i.rect.y = screen_height-450
        if i in good_notes:
            good_sprites_list.add(i)
        else:
            bad_sprites_list.add(i)
        all_sprites_list.add(i)
        my_x += d_x

    my_x = 200
    for i in down_notes:
        i.rect.x = my_x
        i.rect.y = screen_height-150
        if i in good_notes:
            good_sprites_list.add(i)
        else:
            bad_sprites_list.add(i)
        all_sprites_list.add(i)
        my_x += d_x


\
##    for i in range(10 * level):
##
##        bad_sprite = Block("bee.png")
##
##        
##
##        bad_sprite.rect.x = random.randrange(screen_width, screen_width * 2)
##
##        bad_sprite.rect.y = random.randrange(screen_height)
##
##
##        bad_sprites_list.add(bad_sprite)
##
##        all_sprites_list.add(bad_sprite)




# This will clear out all the sprites when the game has ended                   

def empty():

    all_sprites_list.empty()

    bad_sprites_list.empty()

    good_sprites_list.empty()

    



done = False


clock = pygame.time.Clock()


score = 0


lives = 5


## The scroller object is created here

#any_scroller = Scroller(screen_width, 300, screen_height, (255, 100, 100), 2)


## Font to allow for 

font = pygame.font.SysFont("Gill Sans", 25, True, False)


level = 1


# Blocks for first run of game

make_sprites(level)


# Variable to check if pressing r will restart game

can_restart = False


# Variable to check if pressing n will go on to the next level

next_level = False

bgOne = pygame.image.load('Line1.png')
bgTwo = pygame.image.load('Line2.png')

bgOne_x = 0
bgTwo_x = bgOne.get_width()

x = 400
y = 400
    
while not done:

    for event in pygame.event.get(): 

        if event.type == pygame.QUIT: 

            done = True

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_r and can_restart:

                score = 0

                lives = 5

                level = 1

                make_sprites(level)

                can_restart = False

            elif event.key == pygame.K_n and next_level:

                lives = 5

                level += 1

                make_sprites(level)

                next_level = False


    # Clear the screen

    screen.fill(WHITE)

 
    screen.blit(bgOne, (bgOne_x, 0))
    screen.blit(bgTwo, (bgTwo_x, 0))
    
    #pygame.display.update()
 
    bgOne_x -= 1
    bgTwo_x -= 1

      #variables for button placing
    rect_up_bound = [(100, 400), (200, 400), (200, 300), (100, 300)]
    rect_down_bound = [(100, 500), (200, 500), (100, 600), (200, 600)]
    
    #draw buttons
    button_up = pygame.draw.rect(screen, GREEN, (100, 350, 50, 50))
    button_down = pygame.draw.rect(screen, RED, (100, 450, 50, 50))

    #insert sprite here
   # pygame.draw.circle(screen, BLUE, (x, y), 100)
    
    
    #needed for button function
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if pos[0] >= 100 and pos[0] <= 150:
                if pos[1] >= 350 and pos[1] <= 400:
                    player.rect.y -= 155
                elif pos[1] >= 450 and pos[1] <= 500:
                    player.rect.y += 165

##    for event in pygame.event.get():
##        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
##            sys.exit()
## 
##    clock.tick(60)

    # Get the current mouse position. This returns the position

    # as a list of two numbers.

    pos = pygame.mouse.get_pos()



    # Fetch the x and y out of the list,

       # just like we'd fetch letters out of a string.

    # Set the player object to the mouse location

  #  player.rect.midright = pos



    # See if the player block has collided with anything.

    bad_sprites_hit_list = pygame.sprite.spritecollide(player, bad_sprites_list, True)

    good_sprites_hit_list = pygame.sprite.spritecollide(player, good_sprites_list, True)


    # Move the blocks.

    bad_sprites_list.update()

    good_sprites_list.update()



    # Check the list of collisions.

    for block in good_sprites_hit_list:

        score += 1


    for block in bad_sprites_hit_list:

        lives -= 1


    score_text = font.render("Score: " +str(score), True, BLACK)


    lives_text = font.render("Lives: "+ str(lives), True, BLUE)


    screen.blit(score_text, [500, 50])


    screen.blit(lives_text, [50, 50])


    ## Some logic to allow the game to be restarted


    # Check if there are any good sprites left.

    # If not then offer to go on to the next level

    if  len(good_sprites_list) == 0 and lives >= 1:

        empty()

        beat_level = font.render("Congratulations you beat level " + str(level), True, BLACK)

        next_level = font.render("Press 'n' to play the next level", True, BLACK)

        screen.blit(beat_level, [150, 100])

        screen.blit(next_level, [150, 150])

        next_level = True

    

    if lives < 1:

        empty()

        game_over = font.render("Game Over!", True, BLACK)

        play_again = font.render("Press 'r' to play again", True, BLACK)

        screen.blit(game_over, [150, 100])

        screen.blit(play_again, [150, 150])

        can_restart = True

    

    # Draw the scrolling background

##    any_scroller.draw_buildings(screen)
##
##    any_scroller.move_buildings()


    

    # Draw all the sprites  

    all_sprites_list.draw(screen)





   



    # Go ahead and update the screen with what we've drawn.

    pygame.display.flip()



    # Limit to 60 frames per second

    clock.tick(60)


pygame.quit()

exit()


