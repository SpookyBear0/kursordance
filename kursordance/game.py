import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame
from pygame.locals import *
from .circle import ACircle

obj_list = pygame.sprite.Group()
from .objects import obj_list
path = os.path.dirname(os.path.realpath(__file__))
def init(map: str, difficulty: str, mirror: bool):
    pygame.init()

    screen = pygame.display.set_mode((1920, 1080), FULLSCREEN)
    #backdrop = pygame.image.load("").convert()
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        #world.blit(backdrop, backdropbox)
        obj_list.draw(screen) # draw player
        pygame.display.flip()
    pygame.quit()