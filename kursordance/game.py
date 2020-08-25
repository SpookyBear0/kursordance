import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame
from pygame.locals import *

obj_list = pygame.sprite.Group()
path = os.path.dirname(os.path.realpath(__file__))
from .map import *
from .circle import ACircle, Circle
from .slider import Slider
from .spinner import Spinner

def add_approach_circle(x, y):
    circle = ACircle()
    circle.rect.x = x # circle x
    circle.rect.y = y # circle y
    obj_list.add(circle)
    
def add_circle(x, y):
    circle = ACircle()
    circle.rect.x = x # circle x
    circle.rect.y = y # circle y
    obj_list.add(circle)
    
def add_slider(x, y, head, tail, *anchors):
    """doesn't work yet"""
    slider = Slider()
    slider.rect.x = x # slider x
    slider.rect.y = y # slider y
    obj_list.add(slider)
    
def add_spinner(length):
    """doesn't work yet"""
    spinner = Spinner()
    spinner.rect.x = screen.get_width() / 2 # spinner x
    spinner.rect.y = screen.get_height() / 2 # circle y
    obj_list.add(spinner)
screen = pygame.display.set_mode((1920, 1080), FULLSCREEN)
SCREEN_HEIGHT = screen.get_height()
SCREEN_WIDTH = screen.get_width()
def init(map: str, difficulty: str, mirror: bool, download: bool):
    """
    Args:
    map: search query for map
    difficulty: search query for difficulty
    mirror: mirror mode
    download: if kursordance should download the map
    """
    pygame.init()

    #backdrop = pygame.image.load("").convert()
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        screen.fill((0, 0, 0))
        #world.blit(backdrop, backdropbox)
        obj_list.draw(screen) # draw player
        pygame.display.flip()
    pygame.quit()