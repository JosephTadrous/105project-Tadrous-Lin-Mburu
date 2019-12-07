import pygame
import random

class Ball(pygame.sprite.Sprite):
   def __init__(self, color,radius):
       super().__init__()
       self.image=pygame.Surface([30,30])
       self.image.fill((0,0,0))
       self.image.set_colorkey((0,0,0))
       pygame.draw.circle(self.image,color,(0,0),radius)
       self.velocity = [random.randint(10, 20), random.randint(-20, 20)]
       self.circle = self.image.get_rect()

   def update(self):
       self.circle.x += self.velocity[0]
       self.circle.y +=self.velocity[1]

   def bounce(self):
       self.velocity[0]=-self.velocity[0]
       self.velocity[1]=random.randint(-20,20)