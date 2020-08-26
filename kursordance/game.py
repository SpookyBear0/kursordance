import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame
from pygame.locals import *

obj_list = pygame.sprite.Group()
path = os.path.dirname(os.path.realpath(__file__))
screen = pygame.display.set_mode((1920, 1080), FULLSCREEN)
from .circle import ACircle, Circle
from .slider import Slider
from .spinner import Spinner

def add_approach_circle(x, y):
    circle = ACircle()
    circle.rect.x = x * 2.5 + screen.get_height() / 4 # circle x
    circle.rect.y = y * 2.5 # circle y
    obj_list.add(circle)
    
def add_circle(x, y):
    circle = ACircle()
    circle.rect.x = x * 2.5 + screen.get_height() / 4 # circle x
    circle.rect.y = y * 2.5 # circle y
    obj_list.add(circle)
    
def add_slider(x, y):
    return # doesn't work yet
    slider = Slider()
    slider.rect.x = x * 2.5 + screen.get_height() / 4 # slider x
    slider.rect.y = y * 2.5 # slider y
    obj_list.add(slider)
    
def add_spinner(length, x, y):
    #return # doesn't work yet
    spinner = Spinner()
    spinner.rect.x = x + screen.get_height() / 3 # spinner x
    spinner.rect.y = y  # spinner y
    obj_list.add(spinner)
def init(map: str, difficulty: str, mirror: bool, download: bool):
    """
    Args:
    map: search query for map
    difficulty: search query for difficulty
    mirror: mirror mode
    download: if kursordance should download the map
    """
    pygame.init()
    #pygame.display.set_caption(str(osu.Beatmap.artist) + " - " + str(osu.Beatmap.title))
    from . import map
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