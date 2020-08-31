import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame
from pygame.locals import *
from .game import screen

path = os.path.dirname(os.path.realpath(__file__))
i = 100

class Circle(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        circle = pygame.image.load(path + "/assets/hitcircle.png")
        self.circle = pygame.transform.scale(circle, (int(circle.get_width() / 2), int(circle.get_height() / 2)))
        self.rect = circle.get_rect()
        acircle = pygame.image.load(path + "/assets/approachcircle.png")
        self.acircle = pygame.transform.scale(acircle, (int(acircle.get_width()), int(acircle.get_height())))
        self.rect2 = acircle.get_rect()

    def update(self):
        screen.blit(self.acircle, (self.x, self.y))
        screen.blit(self.circle, (self.x, self.y))
    
        
# needs approach circle