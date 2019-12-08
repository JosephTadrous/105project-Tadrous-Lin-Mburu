# Importing pygame package
import pygame
# Importing sound package
import winsound
# Importing Paddle class
from Paddles import Paddle
# Importing Ball class
from Ball import Ball
# Importing package to randomize ball velocity
import random

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
paddleRed = Paddle(RED, 10, 50)
paddleRed.rect.x = 20
paddleRed.rect.y = 250

paddleBlue = Paddle(BLUE, 10, 50)
paddleBlue.rect.x = 670
paddleBlue.rect.y = 250

ball = Ball(WHITE, 10, 10)
ball.rect.x = 340
ball.rect.y = 250

# List of all the sprites to be used
all_sprites_list = pygame.sprite.Group()

# Adding the paddles to the list of sprites
all_sprites_list.add(paddleRed)
all_sprites_list.add(paddleBlue)
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

# Establishing a requirement of condition that will trigger the title screen
Start = 3
# Establishing a requirement of condition that will trigger the main game loop
Run = 0
timer = 0
Person = 0
Computer = 0
Difficulty = 1

# Displaying the initial score:
scoreRed = 0
scoreBlue = 0

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
            if event.key == pygame.K_SPACE:
                # Create a surface object, image is drawn on it
                image = pygame.image.load("/Users/Keith/Downloads/Pygamer credits.png")
                # completely fill the surface object with white colour
                screen.fill(WHITE)
                # copying the image surface object to the display surface object at (0, 0) coordinate.
                screen.blit(image, (0, 0))
                pygame.display.flip()
            if event.key == pygame.K_p:
                if Run == 1:
                    Person = 1
                    Run += 1
                    # Playing main background track when game is started
                    winsound.PlaySound("/Users/Keith/Downloads/backtrack.wav", winsound.SND_ASYNC | winsound.SND_LOOP)
            if event.key == pygame.K_c:
                Computer = 1
                if Run == 1:
                    Run += 1
                    # Playing main background track when game is started
                    winsound.PlaySound("/Users/Keith/Downloads/backtrack.wav", winsound.SND_ASYNC | winsound.SND_LOOP)
            if event.key == pygame.K_e:
                Difficulty = 1
                Run += 1
            if event.key == pygame.K_n:
                Difficulty = 2
                Run += 1
            if event.key == pygame.K_h:
                Difficulty = 3
                Run += 1
            if event.key == pygame.K_r:
                screen.fill(BLACK)
                Start = 3
                Run = 0
                Person = 0
                Computer = 0
                scoreBlue = 0
                scoreRed = 0
            # If return key specifically is pressed
            if event.key == pygame.K_RETURN:
                if Run == 0:  # First return press.
                    Run += 1
                elif Run != 0:
                    Run += 1


    if Run == 3:
        if Person == 1:
            # Clearing the screen
            screen.fill(BLACK)
            # Drawing the score bar
            pygame.draw.line(screen, WHITE, [350, 0], [350, 75], 5)
            pygame.draw.line(screen, WHITE, [700, 75], [0, 75], 10)
            # Drawing the net
            for dash in range(75, 500, 30):
                pygame.draw.line(screen, WHITE, [350, dash - 10], [350, dash], 1)



            # Moving the paddles when player A uses the arrow keys or player B uses the "W/S" keys
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                paddleRed.moveUp(7)
            if keys[pygame.K_s]:
                paddleRed.moveDown(7)
            if keys[pygame.K_UP]:
                paddleBlue.moveUp(7)
            if keys[pygame.K_DOWN]:
                paddleBlue.moveDown(7)

            if ball.rect.x <= 690 and ball.rect.x >= 0:
                if ball.rect.y < 85:
                    ball.velocity[1] = -ball.velocity[1]
                if ball.rect.y > 490:
                    ball.velocity[1] = -ball.velocity[1]
            if ball.rect.x < 0:
                if ball.rect.y < 500 and ball.rect.y > 0:
                    scoreBlue += 1
                    ball.rect.x = 345
                    ball.rect.y = 250
                    paddleBlue.rect.x = 670
                    paddleBlue.rect.y = 250
                    paddleRed.rect.x = 20
                    paddleRed.rect.y = 250
                    Run = 3
                    ball.velocity = [random.randint(15, 15), random.randint(0, 0)]
            if ball.rect.x > 700:
                if ball.rect.y < 500 and ball.rect.y > 0:
                    scoreRed += 1
                    ball.rect.x = 345
                    ball.rect.y = 250
                    paddleBlue.rect.x = 670
                    paddleBlue.rect.y = 250
                    paddleRed.rect.x = 20
                    paddleRed.rect.y = 250
                    Run = 3
                    ball.velocity = [random.randint(15, 15), random.randint(0, 0)]

            if scoreRed >= 5:
                # Playing main background track when game is started
                winsound.PlaySound("/Users/Keith/Downloads/All I Do Is Win.wav", winsound.SND_ASYNC | winsound.SND_LOOP)
                screen.fill(BLACK)
                pygame.display.flip()
                Run = 10
                Start = 12
                Timer = 10
                Person = 10
                text = font3.render("Red wins!", 1, RED)
                screen.blit(text, (250, 90))
                text = font3.render("Do you want to play again?", 1, WHITE)
                screen.blit(text, (60, 200))
                text = font2.render("Press R", 1, WHITE)
                screen.blit(text, (320, 415))
                pygame.display.flip()

            if scoreBlue >= 5:
                # Playing main background track when game is started
                winsound.PlaySound("/Users/Keith/Downloads/All I Do Is Win.wav", winsound.SND_ASYNC | winsound.SND_LOOP)
                screen.fill(BLACK)
                pygame.display.flip()
                Run = 10
                Start = 12
                Timer = 10
                Person = 10
                text = font3.render("Blue wins!", 1, BLUE)
                screen.blit(text, (250, 90))
                text = font3.render("Do you want to play again?", 1, WHITE)
                screen.blit(text, (60, 200))
                text = font2.render("Press R", 1, WHITE)
                screen.blit(text, (300, 415))
                pygame.display.flip()

            if pygame.sprite.collide_mask(ball, paddleRed) or pygame.sprite.collide_mask(ball, paddleBlue):
                ball.bounce()

            text = font.render(str(scoreRed), 1, WHITE)
            screen.blit(text, (175, 1))
            text = font.render(str(scoreBlue), 1, WHITE)
            screen.blit(text, (525, 1))

            all_sprites_list.update()

            # Drawing the sprites
            all_sprites_list.draw(screen)

            # Refreshing screen with lines and sprites
            pygame.display.flip()

            # Passing 30 frames in every second
            clock.tick(30)

        if Computer == 1:
            # Clearing the screen
            screen.fill(BLACK)
            # Drawing the score bar
            pygame.draw.line(screen, WHITE, [350, 0], [350, 75], 5)
            pygame.draw.line(screen, WHITE, [700, 75], [0, 75], 10)
            # Drawing the net
            for dash in range(75, 500, 30):
                pygame.draw.line(screen, WHITE, [350, dash - 10], [350, dash], 1)

            # Moving the paddles when player uses the arrow keys
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                paddleBlue.moveUp(7)
            if keys[pygame.K_DOWN]:
                paddleBlue.moveDown(7)

            if ball.rect.y < paddleRed.rect.y:
                paddleRed.rect.y = paddleRed.rect.y - 2 * random.randint(-1, Difficulty * 2)
                if paddleRed.rect.y < 80:
                    paddleRed.rect.y = 80
                if paddleRed.rect.y > 450:
                    paddleRed.rect.y = 450
            if ball.rect.y > paddleRed.rect.y:
                paddleRed.rect.y = paddleRed.rect.y + 2 * random.randint(-1, Difficulty * 2)
                if paddleRed.rect.y < 80:
                    paddleRed.rect.y = 80
                if paddleRed.rect.y > 450:
                    paddleRed.rect.y = 450

            if ball.rect.x <= 690 and ball.rect.x >= 0:
                if ball.rect.y < 85:
                    ball.velocity[1] = -ball.velocity[1]
                if ball.rect.y > 490:
                    ball.velocity[1] = -ball.velocity[1]
            if ball.rect.x < 0:
                if ball.rect.y < 500 and ball.rect.y > 0:
                    scoreBlue += 1
                    ball.rect.x = 345
                    ball.rect.y = 250
                    paddleBlue.rect.x = 670
                    paddleBlue.rect.y = 250
                    paddleRed.rect.x = 20
                    paddleRed.rect.y = 250
                    Run = 3
                    ball.velocity = [random.randint(5 * Difficulty, 5 * Difficulty), random.randint(0, 0)]
            if ball.rect.x > 700:
                if ball.rect.y < 500 and ball.rect.y > 0:
                    scoreRed += 1
                    ball.rect.x = 345
                    ball.rect.y = 250
                    paddleBlue.rect.x = 670
                    paddleBlue.rect.y = 250
                    paddleRed.rect.x = 20
                    paddleRed.rect.y = 250
                    Run = 3
                    ball.velocity = [random.randint(5 * Difficulty, 5 * Difficulty), random.randint(0, 0)]

            if scoreRed >= 5:
                # Playing main background track when game is started
                winsound.PlaySound("/Users/Keith/Downloads/All I Do Is Win.wav", winsound.SND_ASYNC | winsound.SND_LOOP)
                screen.fill(BLACK)
                pygame.display.flip()
                Run = 10
                Start = 12
                Timer = 10
                Person = 10
                Computer = 10
                text = font3.render("Red wins!", 1, RED)
                screen.blit(text, (250, 90))
                text = font3.render("Do you want to play again?", 1, WHITE)
                screen.blit(text, (60, 200))
                text = font2.render("Press R", 1, WHITE)
                screen.blit(text, (320, 415))
                # # Refreshing screen with text
                # pygame.display.flip()
                # scoreBlue = 0
                # scoreRed = 0
                # text = font.render(str(scoreRed), 1, WHITE)
                # screen.blit(text, (175, 1))
                # text = font.render(str(scoreBlue), 1, WHITE)
                # screen.blit(text, (525, 1))
                # Refreshing screen with text
                pygame.display.flip()
                # if keys[pygame.K_r]:
                #     pass
                # else:

            if scoreBlue >= 5:
                # Playing main background track when game is started
                winsound.PlaySound("/Users/Keith/Downloads/All I Do Is Win.wav", winsound.SND_ASYNC | winsound.SND_LOOP)
                screen.fill(BLACK)
                pygame.display.flip()
                Run = 10
                Start = 12
                Timer = 10
                Person = 10
                Computer = 10
                text = font3.render("Blue wins!", 1, BLUE)
                screen.blit(text, (250, 90))
                text = font3.render("Do you want to play again?", 1, WHITE)
                screen.blit(text, (60, 200))
                text = font2.render("Press R", 1, WHITE)
                screen.blit(text, (300, 415))
                # scoreBlue = 0
                # scoreRed = 0
                # text = font.render(str(scoreRed), 1, WHITE)
                # screen.blit(text, (175, 1))
                # text = font.render(str(scoreBlue), 1, WHITE)
                # screen.blit(text, (525, 1))
                # text = font3.render("Blue wins!", 1, BLACK)
                # screen.blit(text, (250, 90))
                # Refreshing screen with text
                pygame.display.flip()

            if pygame.sprite.collide_mask(ball, paddleRed) or pygame.sprite.collide_mask(ball, paddleBlue):
                ball.bounce()

            text = font.render(str(scoreRed), 1, WHITE)
            screen.blit(text, (175, 1))
            text = font.render(str(scoreBlue), 1, WHITE)
            screen.blit(text, (525, 1))

            all_sprites_list.update()

            # Drawing the sprites
            all_sprites_list.draw(screen)

            # Refreshing screen with lines and sprites
            pygame.display.flip()

            # Passing 60 frames in every second
            clock.tick(60)
    # If Run is 1, meaning that Return has been pressed a second time

    # If Run is still 0, meaning return has not been pressed
    if Run == 2:
        # If Start is still 1, meaning title screen code has yet to run
        while Start == 1:
            if Person == 1:
                Run = 3
            screen.fill(BLACK)
            # Playing title background track on title screen
            winsound.PlaySound("/Users/Keith/Downloads/doot doots.wav", winsound.SND_ASYNC | winsound.SND_LOOP)
            text = font3.render("Select Difficulty Level", 1, WHITE)
            screen.blit(text, (90, 90))
            text1 = font2.render("Easy              Press E", 1, WHITE)
            text2 = font2.render("Normal         Press N", 1, WHITE)
            text3 = font2.render("Hard              Press H", 1, WHITE)
            screen.blit(text1, (270, 315))
            screen.blit(text2, (270, 365))
            screen.blit(text3, (270, 415))
            # Refreshing screen with text
            pygame.display.flip()
            # Changing Start so that title screen displays only once
            Start = 0
    if Run == 1:
        # If Start is still 1, meaning title screen code has yet to run
        while Start == 2:
            # Playing title background track on title screen
            winsound.PlaySound("/Users/Keith/Downloads/doot doots.wav", winsound.SND_ASYNC | winsound.SND_LOOP)
            # Clearing the screen
            screen.fill(BLACK)
            text = font3.render("Do you want to play against a", 1, WHITE)
            screen.blit(text, (20, 90))
            text = font3.render("person or the computer?", 1, WHITE)
            screen.blit(text, (70, 150))
            text = font2.render("Press P or C", 1, WHITE)
            screen.blit(text, (290, 415))
            # Refreshing screen with text
            pygame.display.flip()
            # Changing Start so that title screen displays only once
            Start = 1
    if Run == 0:
        # If Start is still 1, meaning title screen code has yet to run
        while Start == 3:
            screen.fill(BLACK)
            # Playing title background track on title screen
            winsound.PlaySound("/Users/Keith/Downloads/doot doots.wav", winsound.SND_ASYNC | winsound.SND_LOOP)
            text = font1.render("Pong V2", 1, WHITE)
            screen.blit(text, (90, 90))
            text = font2.render("Press Enter to start", 1, WHITE)
            screen.blit(text, (270, 415))
            # Refreshing screen with text
            pygame.display.flip()
            # Changing Start so that title screen displays only once
            Start = 2




# Stopping game engine when Continue is False
pygame.quit()



























