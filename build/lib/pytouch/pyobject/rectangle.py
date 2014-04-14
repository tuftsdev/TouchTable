import pygame
from pyobject import *

class Rectangle(PyObject):

    def __init__(self, x, y, width, height, color='white', alpha=None, z_index=0, drag_enabled=False, edge_thickness=0):
        super(Rectangle,self).__init__(x, y, width, height, z_index, drag_enabled)

        self.color = pygame.Color(color)
        self.edge_thickness = edge_thickness
        self.alpha = alpha
        self.image = pygame.Surface((width, height))
        self.image.set_alpha(alpha)
        self.image.fill(self.color)

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def changeColor(self, r, g, b, a):
        self.color = pygame.Color(r,g,b,a)

    def changeColor(self, color, g=None, b=None, a=None):
        if g is None or b is None or a is None:
            self.color = pygame.Color(color)
        else:
            self.color = pygame.Color(color, g, b, a)

    def setAlpha(self, alpha):
        self.alpha = alpha
        self.image.set_alpha(alpha)
