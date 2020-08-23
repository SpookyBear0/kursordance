import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame
from pygame.locals import *

path = os.path.dirname(os.path.realpath(__file__))

class Spinner(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        spinner = pygame.image.load(path + "/assets/spinner-circle.png")
        self.images.append(spinner)
        self.image = self.images[0]
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() / 2), int(self.image.get_height() / 2)))
        self.rect = self.image.get_rect()
    def update(self):
        pass
    
    
# needs approach circle