import pygame
from pyobject import *

class Circle(PyObject):

    def __init__(self, center, radius, z_index=0,drag_enabled=False, color='white', edge_thickness=0):

    	# TODO: TYPE CHECKING ON CENTER, OF TYPE TUPLE (TYPE) AND LENGTH 2 (LEN)
    	self.center = center
        self.radius = radius
        super(Circle,self).__init__(center[0]-radius, center[1]-radius, radius * 2, radius * 2, z_index, drag_enabled)

        self.color = pygame.Color(color)
        self.edge_thickness = edge_thickness

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.center, self.radius, self.edge_thickness)

    def dragHandler(self, obj, touch, extra=None):
        if self.drag_enabled:
            self.move(touch.xpos, touch.ypos)

    def move(self, x, y):
        self.center = (x, y)
        self.x = x - self.radius
        self.y = y - self.radius

    def changeColor(self, r, g, b, a):
        self.color = pygame.Color(r,g,b,a)

    def changeColor(self, color, g=None, b=None, a=None):
        if g is None or b is None or a is None:
            self.color = pygame.Color(color)
        else:
            self.color = pygame.Color(color, g, b, a)
