# Importing pygame package
import pygame
# Importing sound package
import winsound
# Importing Paddle class
from Paddles import Paddle

# Initialising game engine
pygame.init()

# Creating and naming the Pong window
screen = pygame.display.set_mode((700, 500), pygame.FULLSCREEN)
pygame.display.set_caption("Pong v2")

# Hiding pointer so it does not get in the way
pygame.mouse.set_visible(False)

# Defining the four colors used
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
RED = (255,0,0)

# Creating two paddles, one for each player
# Assigning the respective colors
# Establishing the positions of the paddles
paddleA = Paddle(RED, 10, 50)
paddleA.rect.x = 20
paddleA.rect.y = 250

paddleB = Paddle(BLUE, 10, 50)
paddleB.rect.x = 670
paddleB.rect.y = 250

# List of all the sprites to be used
all_sprites_list = pygame.sprite.Group()

# Adding the paddles to the list of sprites
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)

# Using clock to set the number of times screen updates each second
clock = pygame.time.Clock()

# Setting a boolean that controls when the game is open or closed
Continue = True

# Setting the fonts and font sizes to be used for title screen and scores
font = pygame.font.Font("/Users/Keith/Downloads/product-sans/Product Sans Regular.ttf", 60)
font1 = pygame.font.Font("/Users/Keith/Downloads/zorque/zorque.ttf", 120)
font2 = pygame.font.Font("/Users/Keith/Downloads/product-sans/Product Sans Regular.ttf", 20)

# Establishing a requirement of condition that will trigger the title screen
Start = 1
# Establishing a requirement of condition that will trigger the main game loop
Run = 0
# Running game until Continue is False
while Continue:
    events = pygame.event.get()
    for event in events:
        # If exit button is clicked
        if event.type == pygame.QUIT:
            # Breaking the loop, closing the game
            Continue = False
        # If any key is being pressed
        if event.type == pygame.KEYDOWN:
            # If m button is clicked
            if event.key == pygame.K_m:
                # Exiting fullscreen mode
                screen = pygame.display.set_mode((700, 500))
            # If Esc button is clicked
            if event.key == pygame.K_ESCAPE:
                # Breaking the loop, closing the game
                Continue = False
            # If return key specifically is pressed
            if event.key == pygame.K_RETURN:
                Run += 1  # Allowing main game loop to run

    if Run == 1:
        # Playing main background track when game is started
        winsound.PlaySound("/Users/Keith/Downloads/backtrack.wav", winsound.SND_ASYNC | winsound.SND_LOOP)
        # Clearing the screen and redrawing net and score bar
        screen.fill(BLACK)
        pygame.display.flip()
        # Drawing the net
        pygame.draw.line(screen, WHITE, [350, 0], [350, 75], 5)
        # Drawing the score bar
        pygame.draw.line(screen, WHITE, [700, 75], [0, 75], 10)
        for dash in range(75, 500, 30):
            pygame.draw.line(screen, WHITE, [350, dash - 10], [350, dash], 1)

        all_sprites_list.update()

        # Now let's draw all the sprites in one go. (For now we only have 2 sprites!)
        all_sprites_list.draw(screen)

        # Displaying the initial score:
        scoreA = 0
        scoreB = 0
        text = font.render(str(scoreA), 1, WHITE)
        screen.blit(text, (175, 1))
        text = font.render(str(scoreB), 1, WHITE)
        screen.blit(text, (525, 1))

        keys = pygame.key.get_pressed()
        # Moving the paddles when player A uses the arrow keys or player B uses the "W/S" keys
        if keys[pygame.K_w]:
            paddleA.moveUp(5)
        if keys[pygame.K_s]:
            paddleA.moveDown(5)
        if keys[pygame.K_UP]:
            paddleB.moveUp(5)
        if keys[pygame.K_DOWN]:
            paddleB.moveDown(5)

        all_sprites_list.update()

        # Now let's draw all the sprites in one go. (For now we only have 2 sprites!)
        all_sprites_list.draw(screen)

        # Refreshing screen with lines and sprites
        pygame.display.flip()

        # Passing 30 frames in every second
        clock.tick(120)
    # If Run is still 0, meaning return has not been pressed
    else:
        # If Start is still 1, meaning title screen code has yet to run
        while Start:
            # Playing title background track on title screen
            winsound.PlaySound("/Users/Keith/Downloads/doot doots.wav", winsound.SND_ASYNC | winsound.SND_LOOP)
            text = font1.render("Pong v2", 1, WHITE)
            screen.blit(text, (90, 90))
            text = font2.render("Press Enter to start", 1, WHITE)
            screen.blit(text, (255, 415))
            # Refreshing screen with text
            pygame.display.flip()
            # Changing Start so that title screen displays only once
            Start = 0

# Stopping game engine when Continue is False:
pygame.quit()























