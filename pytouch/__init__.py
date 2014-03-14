import sys
import pygame, touch, pyobject
from pygame.locals import *

def init():
    return PyTouch()

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
        self.draggedObject.dragHandler(self.draggedObject, t)
      else:
        for obj in self.objects:
          if obj.touchInside(t):
            if t.status == "dragging":
              self.draggedObject = obj
            else:
              self.draggedObject = None
            break
    self.clear()
    self.redraw()
    self.sortObjects()
    pygame.display.flip()

  def redraw(self, obj_ignore=None):
    for obj in reversed(self.objects):
      if obj != obj_ignore:
        obj.draw(self.screen)

  def drawRect(self, x, y, width, height, z_index=0,drag_enabled=False,color='white', edge_thickness=0):
    newRect = pyobject.Rectangle(x,y,width,height,z_index,drag_enabled,color,edge_thickness)
    self.objects.append(newRect)
    return newRect

  def drawImage(self, image, x, y, z_index=0, drag_enabled=False):
    newImage = pyobject.Image(image, x, y, z_index, drag_enabled)
    self.objects.append(newImage)
    return newImage

  def sortObjects(self):
    self.objects = sorted(self.objects, key=lambda obj: obj.z_index, reverse=True)

  def clear(self):
    self.screen.fill(self.bgcolor)
