import sys
import pygame, touch, pyobject
from pygame.locals import *


class PyTouch(object):
  def __init__(self, bgcolor=(0,0,0)):
    pygame.init()
    self.screen = pygame.display.set_mode((800,600), pygame.FULLSCREEN)
    self.touchTracker = touch.TouchTracker(pygame.display.Info().current_w,pygame.display.Info().current_h)
    self.objects = []
    self.bgcolor = bgcolor
    self.draggedObject = None
    self.clear()

  def update(self):
    t = self.touchTracker.update()
    if t != None:
      if self.draggedObject is not None and t.status == "dragging":
        self.draggedObject.dragHandler(t, self.draggedObject)
      else:
        for obj in self.objects:
          if obj.touchUpInside(t):
            if t.status == "dragging":
              self.draggedObject = obj
            else:
              self.draggedObject = None
            break
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
