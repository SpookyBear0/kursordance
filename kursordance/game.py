import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame
from pygame.locals import *
from .circle import Circle
circle = Circle()
circle.rect.x = 0
circle.rect.y = 0
obj_list = pygame.sprite.Group()
obj_list.add(circle)

path = os.path.dirname(os.path.realpath(__file__))

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