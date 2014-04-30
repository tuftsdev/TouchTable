from pygame.time import *

class Clock():
    def __init__(self):
        self.clock = pygame.time.Clock()

    def tick(self, framerate):
        self.clock.tick(framerate)

    def tick_busy_loop(self, framerate):
        self.clock.tick_busy_loop(framerate)

    def get_time(self):
        return self.clock.get_time()

    def get_rawtime(self):
        return self.clock.get_rawtime()

    def get_fps(self):
        return self.clock.get_fps()
