# Importing pygame package
import pygame
# Importing sound package
import winsound
# Importing Paddle class
from Paddles import Paddle
from Ball import Ball

# Initialising game engine
pygame.init()

# Creating and naming the Pong window
screen = pygame.display.set_mode((700, 500), pygame.FULLSCREEN)
pygame.display.set_caption("Pong V2")

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

ball=Ball(WHITE,10,10)
ball.rect.x=340
ball.rect.y=250

# List of all the sprites to be used
all_sprites_list = pygame.sprite.Group()

# Adding the paddles to the list of sprites
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)

# Using clock to set the number of times screen updates each second
clock = pygame.time.Clock()



# Setting a boolean that controls when the game is open or closed
Continue = True

# Setting the fonts and font sizes to be used for title screen and scores
font = pygame.font.Font("/Users/Keith/Downloads/product-sans/Product Sans Regular.ttf", 60)
font1 = pygame.font.Font("/Users/Keith/Downloads/zorque/zorque.ttf", 120)
font2 = pygame.font.Font("/Users/Keith/Downloads/product-sans/Product Sans Regular.ttf", 20)
font3 = pygame.font.Font("/Users/Keith/Downloads/zorque/zorque.ttf", 40)

keys = pygame.key.get_pressed()

# Establishing a requirement of condition that will trigger the title screen
Start = 2
# Establishing a requirement of condition that will trigger the main game loop
Run = 0
timer = 0
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
                    if timer == 0:  # First return press.
                        timer = 0.001  # Start the timer.
                    # Press again before 0.5 seconds to double press.
                    elif timer < 5:
                        print('double press')
                        timer = 0
                        Run += 2  # Starting main game loop
                        # Playing main background track when game is started
                        winsound.PlaySound("/Users/Keith/Downloads/backtrack.wav", winsound.SND_ASYNC | winsound.SND_LOOP)



    # Increase timer after mouse was pressed the first time.
    if timer != 0:
        timer += 0.1
        # Reset after 0.5 seconds.
        if timer >= 5:
            Run += 1  # Allowing person vs computer choice
            timer = 0

    if Run == 2:
        # Clearing the screen
        screen.fill(BLACK)
        # Drawing the score bar
        pygame.draw.line(screen, WHITE, [350, 0], [350, 75], 5)
        pygame.draw.line(screen, WHITE, [700, 75], [0, 75], 10)
        # Drawing the net
        for dash in range(75, 500, 30):
            pygame.draw.line(screen, WHITE, [350, dash - 10], [350, dash], 1)

        # Displaying the initial score:
        scoreA = 0
        scoreB = 0
        text = font.render(str(scoreA), 1, WHITE)
        screen.blit(text, (175, 1))
        text = font.render(str(scoreB), 1, WHITE)
        screen.blit(text, (525, 1))

        # Moving the paddles when player A uses the arrow keys or player B uses the "W/S" keys
        if keys[pygame.K_w]:
            paddleA.moveUp(5)
        if keys[pygame.K_s]:
            paddleA.moveDown(5)
        if keys[pygame.K_UP]:
            paddleB.moveUp(5)
        if keys[pygame.K_DOWN]:
            paddleB.moveDown(5)

        if ball.rect.x <= 700 and ball.rect.x >= 0:
            if ball.rect.y<0:
                ball.velocity[1] = -ball.velocity[1]
            if ball.rect.y>500:
                ball.velocity[1] = -ball.velocity[1]
        if ball.rect.x<0:
            if ball.rect.y<500 and ball.rect.y>0:
                scoreA += 1
                ball.rect.x = 345
                ball.rect.y = 250
                Run=2
        if ball.rect.x >700:
            if ball.rect.y < 500 and ball.rect.y > 0:
                scoreB += 1
                ball.rect.x = 345
                ball.rect.y = 250
                Run=2
                
        all_sprites_list.update()

        # Drawing the sprites
        all_sprites_list.draw(screen)

        # Refreshing screen with lines and sprites
        pygame.display.flip()

        # Passing 30 frames in every second
        clock.tick(30)
    # If Run is still 0, meaning return has not been pressed
    if Run == 0:
        # If Start is still 1, meaning title screen code has yet to run
        while Start == 2:
            # Playing title background track on title screen
            winsound.PlaySound("/Users/Keith/Downloads/doot doots.wav", winsound.SND_ASYNC | winsound.SND_LOOP)
            text = font1.render("Pong V2", 1, WHITE)
            screen.blit(text, (90, 90))
            text = font2.render("Press Enter to start", 1, WHITE)
            screen.blit(text, (270, 415))
            # Refreshing screen with text
            pygame.display.flip()
            # Changing Start so that title screen displays only once
            Start = 1
    # If Run is 1, meaning that Return has been pressed a second time
    if Run == 1:
        # If Start is still 1, meaning title screen code has yet to run
        while Start == 1:
            # Playing title background track on title screen
            winsound.PlaySound("/Users/Keith/Downloads/doot doots.wav", winsound.SND_ASYNC | winsound.SND_LOOP)
            # Clearing the screen
            screen.fill(BLACK)
            text = font3.render("Do you want to play against a", 1, WHITE)
            screen.blit(text, (20, 90))
            text = font3.render("person or the computer?", 1, WHITE)
            screen.blit(text, (70, 150))
            text = font2.render("Press P or C", 1, WHITE)
            screen.blit(text, (300, 415))
            # Refreshing screen with text
            pygame.display.flip()
            # Changing Start so that title screen displays only once
            Start = 0

# Stopping game engine when Continue is False:
pygame.quit()



























