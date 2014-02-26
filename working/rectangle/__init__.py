import pygame

class Rectangle(object):
  def __init__(self, surface, x, y, width, height, color='white', edge_thickness=0):
    self.box = pygame.Rect(x, y, width, height)
    self.surface = surface
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.color = pygame.Color(color)
    self.edge_thickness = edge_thickness
    self.draw()

  def draw(self):
    pygame.draw.rect(self.surface, self.color, self.box, self.edge_thickness)

  def touchUpInside(self, touch):
    if(touch.xpos >= self.box.left and touch.xpos <= self.box.right and touch.ypos >= self.box.top and touch.ypos <= self.box.bottom):
      return self.touchUpInsideHandler(touch,self)

  def changeColor(self, color):
    self.color = pygame.Color(color)
    self.draw()


  def touchUpInsideHandler(self, touch, extra=None):
    return True
