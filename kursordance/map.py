import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame
from pygame.locals import *
from .game import add_slider, add_spinner, add_circle
from osu import beatmap, objects
from threading import Thread

map_osu_path = "D:\games\osu!\Songs\941085 tieff - Our Story\\tieff - Our Story (Hinsvar) [Insane].osu"
map = beatmap.Beatmap(map_osu_path)
objectlist = map.hitObjects
timing = map.timingPoints
def map_thread(): # in a thread so we can use timer
    for o in objectlist:
        if isinstance(o, objects.Circle):
            print("circle")
            add_circle(o.x, o.y)
        elif isinstance(o, objects.Slider):
            print("slider")
            add_slider(o.x, o.y)
        elif isinstance(o, objects.Spinner):
            print("spinner")
            add_spinner(o.time - o.endTime, o.x, o.y)

Thread(target=map_thread).start()

# add map stuff here realistik
