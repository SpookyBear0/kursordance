import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame
from pygame.locals import *

path = os.path.dirname(os.path.realpath(__file__))

class Circle(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        img = pygame.image.load(path + "/assets/hitcircle.png")
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
    def update(self):
        pass