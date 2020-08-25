import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
from .circle import Circle
import pygame
from pygame.locals import *
import osu

pygame.display.set_caption(str(osu.Beatmap.artist) + " - " + str(osu.Beatmap.title))

# add map stuff here realistik
