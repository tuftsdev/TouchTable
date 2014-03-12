import pygame

class Rectangle(object):
  def __init__(self, surface, x, y, width, height, color='white', z_index=0, edge_thickness=0):
    self.box = pygame.Rect(x, y, width, height)
    self.surface = surface
    self.x = x
    self.y = y
    self.z_index = z_index
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

<<<<<<< HEAD
  def changeColor(self, color):
    self.color = pygame.Color(color)
    self.draw()

    self.dirty = True

  def changeColor(self, r, g, b, a):
    self.color = pygame.Color(r,g,b,a)
=======
  def changeColor(self, color, g=None, b=None, a=None):
    if g is None or b is None or a is None:
      self.color = pygame.Color(color)
    else:
      self.color = pygame.Color(color,g,b,a)
>>>>>>> 9ea4266ba364147e568060fbdeed4369cfc4f2a4
    self.draw()

    self.dirty = True


