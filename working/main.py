import pygame, touch, rectangle
from pygame.locals import *
from pprint import pprint

class PyTouch(object):
  def __init__(self):
    pygame.init()
    self.screen = pygame.display.set_mode((800,600))
    self.touchTracker = touch.TouchTracker(800,600)
    self.objects = []

  def update(self):
    t = self.touchTracker.update()
    if t != None:
      for obj in self.objects:
        if obj.touchUpInside(t):
          print "Touched!"
    pygame.display.flip()

  def drawRect(self, x, y, width, height, color='white', edge_thickness=0, surface=None):
    if surface == None:
      surface = self.screen
    newRect = rectangle.Rectangle(surface,x,y,width,height,color,edge_thickness)
    self.objects.append(newRect)
    return newRect

def touch_handler(touch, self):
  self.changeColor('blue')

if __name__ == "__main__":
  pytouch = PyTouch()
  rect = pytouch.drawRect(300,300,40,60)
  rect.touchUpInsideHandler = touch_handler
  while 1:
    pytouch.update()

