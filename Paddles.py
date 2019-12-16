import pygame
BLACK = (0,0,0)

class Paddle(pygame.sprite.Sprite):
   # This class represents the paddle. It uses the "Sprite" class in Pygame.
   def __init__(self, color, width, height):
       # to initialize the main properties of the object
       super().__init__()
       # calling the "Sprite" class constructor
       self.image = pygame.Surface([width, height])
       self.image.fill(BLACK)
       self.image.set_colorkey(BLACK)
       # set the width and height of the surface
       # set the background color to black
       pygame.draw.rect(self.image, color, [0, 0, width, height])
       # draw the paddle on the surface and initialize its position at (0,0) with dimensions:(width,height)
       self.rect = self.image.get_rect()
       # fetch the rectangle object that has the dimensions of the image.
   def moveUp(self, pixels): # this method is used to move the paddles up by changing their pixels which are also their positions
       self.rect.y -= pixels #while the paddles are moving up, only their y-component pixels will decrease
       if self.rect.y < 80:  # the following section of code make sures that paddles will not move outside of the top of the screen 
           self.rect.y = 80
       

   def moveDown(self, pixels):# this method is used to move the paddles down by changing their pixels which are also their positions
       self.rect.y += pixels #while the paddles are moving down, only their y-component pixels will increase
       if self.rect.y > 450: # the following section of code make sures that paddles will not move outside of bottom of the screen
           self.rect.y = 450

