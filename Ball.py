import pygame
from random import randint

BLACK = (0, 0, 0)


class Ball(pygame.sprite.Sprite):
    # This class represents a car. It derives from the "Sprite" class in Pygame.

    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # Draw the ball (a rectangle!)
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.velocity = [randint(4, 6), randint(-6, 6)]

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-6, 6)


# black=(0,0,0)
# class Ball(pygame.sprite.Sprite):
#     def __init__(self, color,radius):
#         super().__init__()
#         self.image=pygame.Surface([30,30])
#         self.image.fill(black)
#         self.image.set_colorkey(black)
#         pygame.draw.circle(self.image,color,(0,0),radius)
#         self.velocity = [random.randint(10, 20), random.randint(-20, 20)]
#         self.circle = self.image.get_rect()
#
#     def update(self):
#         self.circle.x += self.velocity[0]
#         self.circle.y +=self.velocity[1]
#
#     def bounce(self):
#         self.velocity[0]=-self.velocity[0]
#         self.velocity[1]=random.randint(-20,20)


