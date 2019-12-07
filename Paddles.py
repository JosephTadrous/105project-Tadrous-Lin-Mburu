import pygame
BLACK = (0,0,0)

class Paddle(pygame.sprite.Sprite):
   # This class represents the paddle. It uses the "Sprite" class in Pygame.
   def __init__(self, color, width, height):
       # to initalise the main properties of the object
       super().__init__()
       # calling the "Sprite" class constructor
       self.image = pygame.Surface([width, height])
       self.image.fill(BLACK)
       self.image.set_colorkey(BLACK)
       # set the width and height of the surface
       # set the background color to black
       pygame.draw.rect(self.image, color, [0, 0, width, height])
       # draw the paddle on the surface and initalise its position at (0,0) with dimensions:(width,height)
       self.rect = self.image.get_rect()
       # fetch the rectangle object that has the dimensions of the image.
   def moveUp(self, pixels): # method
       self.rect.y -= pixels
       if self.rect.y < 85:
           self.rect.y = 85
       # Check that you are not going too far (off the screen)

   def moveDown(self, pixels):
       self.rect.y += pixels
       if self.rect.y > 440:
           self.rect.y = 440
