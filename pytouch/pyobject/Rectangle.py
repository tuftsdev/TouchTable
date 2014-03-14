import pygame
from pyobject import *

class Rectangle(PyObject):

    def __init__(self, x, y, width, height, z_index=0,drag_enabled=False, color='white', edge_thickness=0):
        super(Rectangle,self).__init__(x, y, width, height, z_index, drag_enabled)

        self.color = pygame.Color(color)
        self.edge_thickness = edge_thickness

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, self.edge_thickness)

    def changeColor(self, r, g, b, a):
        self.color = pygame.Color(r,g,b,a)

    def changeColor(self, color, g=None, b=None, a=None):
        if g is None or b is None or a is None:
            self.color = pygame.Color(color)
        else:
            self.color = pygame.Color(color, g, b, a)
