import sys
import pygame, touch, pyobject
from pygame.locals import *


class PyTouch(object):
  def __init__(self, bgcolor=(0,0,0)):
    pygame.init()
    self.screen = pygame.display.set_mode((800,600))
    self.touchTracker = touch.TouchTracker(800,600)
    self.objects = []
    self.bgcolor = bgcolor
    self.clear()

  def update(self):
    t = self.touchTracker.update()
    if t != None:
      for obj in self.objects:
        obj.touchUpInside(t)
    self.clear()
    self.redraw()
    pygame.display.flip()

  def redraw(self, obj_ignore=None):
    for obj in self.objects:
      if obj != obj_ignore:
        obj.draw()

  def drawRect(self, x, y, width, height, color='white', edge_thickness=0, surface=None):
    if surface == None:
      surface = self.screen
    newRect = pyobject.Rectangle(surface,x,y,width,height,color,edge_thickness)
    self.objects.append(newRect)
    return newRect

  def clear(self):
    self.screen.fill(self.bgcolor)
