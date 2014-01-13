import pygame
from pygame.time import *

class Clock():
    def __init__(self):
        self.clock = pygame.time.Clock()

    def tick(framerate):
        self.clock.tick(framerate)

    def tick_busy_loop(framerate):
        self.clock.tick_busy_loop(framerate)

    def get_time():
        return self.clock.get_time()

    def get_rawtime():
        return self.clock.get_rawtime()

    def get_fps():
        return self.clock.get_fps()

def 
