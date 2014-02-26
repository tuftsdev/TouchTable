__all__ = ["Clock"]

import pygame
from pygame.time import *

def get_ticks():
    return pygame.time.get_ticks()

def wait(milliseconds):
    pygame.time.wait(milliseconds)

def delay(milliseconds):
    pygame.time.delay(milliseconds)

def set_timer(eventid, milliseconds):
    pygame.time.set_timer(eventid, milliseconds)
