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

    self.dirty = False

  def draw(self):
    pygame.draw.rect(self.surface, self.color, self.box, self.edge_thickness)

  def move(self, x, y):
    self.box = self.box.move(x-self.x, y-self.y)
    self.draw()
    self.x = x
    self.y = y

    self.dirty = True

  def touchUpInside(self, touch):
    if(touch.xpos >= self.box.left and touch.xpos <= self.box.right and touch.ypos >= self.box.top and touch.ypos <= self.box.bottom):
      if touch.status == "dragging":
        self.dragHandler(touch,self)
      elif touch.status == "holding":
        self.holdHandler(touch,self)
      elif touch.status == "clicked":
        self.touchUpInsideHandler(touch,self)
      return True

  def touchUpInsideHandler(self, touch, extra=None):
    return True

  def dragHandler(self, touch, extra=None):
    return True

  def holdHandler(self, touch, extra=None):
    return True

  def changeColor(self, color):
    self.color = pygame.Color(color)
    self.draw()

    self.dirty = True

  def changeColor(self, r, g, b, a):
    self.color = pygame.Color(r,g,b,a)
    self.draw()

    self.dirty = True


