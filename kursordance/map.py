import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
from .circle import Circle
import pygame
from pygame.locals import *

# add map stuff here realistik
circle = Circle()
circle.rect.x = 0
circle.rect.y = 0
obj_list = pygame.sprite.Group()
obj_list.add(circle)