import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame
from pygame.locals import *

path = os.path.dirname(os.path.realpath(__file__))
i = 100

class Circle(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        circle = pygame.image.load(path + "/assets/hitcircle.png")
        self.images.append(circle)
        self.image = self.images[0]
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() / 2), int(self.image.get_height() / 2)))
        self.rect = self.image.get_rect()

    def update(self):
        pass
    
class ACircle(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        circle = pygame.image.load(path + "/assets/approachcircle.png")
        self.images.append(circle)
        self.image = self.images[0]
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width()), int(self.image.get_height())))
        self.rect = self.image.get_rect()
        
    def update(self):
        global i
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() - i), int(self.image.get_height() - i)))
        i -= 1
        
# needs approach circle