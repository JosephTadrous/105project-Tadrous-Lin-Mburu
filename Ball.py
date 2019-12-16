import pygame
from random import randint

BLACK = (0, 0, 0)#define color


class Ball(pygame.sprite.Sprite):
   

    def __init__(self, color, width, height):
        # Call the parent class (Sprite) 
        super().__init__()

        # Define the properties of the ball: x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # Draw the ball 
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.velocity = [randint(8, 10), randint(-10, 10)]

        # Fetch the rectangle object which is the ball
        self.rect = self.image.get_rect()

    def update(self):# this functions will update the position of the ball
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):#this functions changes the velocity of the ball
        self.velocity[0] = -self.velocity[0]#the x-component of the velocity is reversed
        self.velocity[1] = randint(-10, 10)#the y-component velocity is randomly reassigned without changing its direction

        


