import pygame
from pyobject import *

class Image(PyObject):
    def __init__(self, image, x, y, z_index=0, drag_enabled=False):
        self.image = pygame.image.load(image)
        self.image_rect = self.image.get_rect()
        super(Image,self).__init__(x, y, self.image_rect.width, self.image_rect.height, z_index, drag_enabled)

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def convert(self):
        self.image.convert()

    def convert_alpha(self):
        self.image.convert_alpha()
