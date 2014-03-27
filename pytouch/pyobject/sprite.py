import pygame
from pyobject import *

class SpriteAnim(PyObject):
    def __init__(self, image, x, y, frame_x, frame_y, frame_width, frame_height, delay=5, z_index=0, drag_enabled=False):
        self.image = pygame.image.load(image)

    # Initial frame
        self.frame_rect = pygame.Rect(frame_x, frame_y, frame_width, frame_height)
        self.framelist = [self.image.subsurface(self.frame_rect)]

        self.frame_count = 1
        self.curr_frame = -1 # ensures first frame is drawn

        self.playing = False
        self.repeat = False
        self.delay = delay # Switch frame every x frames
        self.delay_counter = 0

        self.frame_width = frame_width
        self.frame_height = frame_height

        super(Image,self).__init__(x, y, self.frame_width, self.frame_height, z_index, drag_enabled)

# If it draws the last frame first, means that curr_frame is -1, did not update first
    def draw(self, surface):
        if self.playing:
            surface.blit(self.framelist[self.curr_frame], self.x, self.y)

# Must update before drawing
    def update(self):
        if self.playing:
            if self.curr_frame >= self.frame_count:
                self.curr_frame = 0
                if not self.repeat:
                    self.playing = False
            else:
                if self.delay_counter == self.delay:
                    self.delay_counter = 0
                    self.curr_frame += 1
                else:
                    self.delay_counter += 1
# Stores unaltered update function.  If a new update function is to be
# defined, call _update at the end
    _update = update

    def startAnimation(self, repeat=False):
        self.playing = True
        self.repeat = repeat

    def stopAnimation(self):
        self.playing = False

    def loadFrame(self, frame_x, frame_y, pos=-1):
        new_frame = self.image.subsurface(pygame.Rect(frame_x, frame_y, self.frame_width, self.frame_height))
        self.frame_count += 1
        if pos < 0:
            self.framelist.append(new_frame)
        else:
            self.framelist.insert(pos, new_frame)

    def removeFrame(self, frame_num):
        self.framelist.pop(frame_num)
        self.frame_count -= 1

    def setCurrentFrame(self, x):
        self.curr_frame = x

    def setDelay(self, delay):
        self.delay = delay

    def isPlaying(self):
        return self.playing

    def convert_alpha(self):
        self.image.convert_alpha()

    def convert_alpha_all(self):
        self.image.convert_alpha()
        for frame in self.framelist:
            frame.convert_alpha()

