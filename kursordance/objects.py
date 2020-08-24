import pygame
from pygame.locals import *
from .circle import ACircle, Circle
from .slider import Slider
from .spinner import Spinner
from .game import obj_list, screen

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