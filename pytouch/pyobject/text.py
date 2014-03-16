import pygame
from pyobject import *

class Text(PyObject):

    def __init__(self, x, y, text, fontsize, fontcolor, font=None, aa=1, z_index=0, drag_enabled=False):
        self.text = text
        if font == None:
            self.font = pygame.font.Font(None, fontsize)
        else:
            self.font.SysFont(font, fontsize)
        self.textrender = self.font.render(text, aa, fontcolor) # Color (255,255,255)
        self.text_rect = self.textrender.get_rect()
        super(Text,self).__init__(x, y, self.text_rect.width, self.text_rect.height, z_index, drag_enabled)

    def draw(self, surface):
        surface.blit(self.textrender, (self.x, self.y))
