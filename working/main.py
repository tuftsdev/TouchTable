import pygame, touch, rectangle
import random
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
    pygame.display.flip()

  def drawRect(self, x, y, width, height, color='white', edge_thickness=0, surface=None):
    if surface == None:
      surface = self.screen
    newRect = rectangle.Rectangle(surface,x,y,width,height,color,edge_thickness)
    self.objects.append(newRect)
    return newRect

  def clear(self):
    self.screen.fill(self.bgcolor)

def touch_handler(touch, self):
  self.changeColor('red')

if __name__ == "__main__":
  pytouch = PyTouch()
  timer = 0
  for i in range(0, 3):
    for j in range(0, 3):
      pytouch.drawRect(j*150+150, i*150+150, 100,100)
  x = random.randint(0,2)
  y = random.randint(0,2)
  rect = pytouch.drawRect(x*150+150+10, y*150+150+10,80,80, 'blue')
  rect.touchUpInsideHandler = touch_handler

  timer_max = random.randint(50,100)
  while 1:
    if timer > timer_max:
      timer_max = random.randint(50,100)
      pytouch.clear()
      for i in range(0, 3):
        for j in range(0, 3):
          pytouch.drawRect(j*150+150, i*150+150, 100,100)
      timer = 0
      x = random.randint(0,2)
      y = random.randint(0,2)
      rect = pytouch.drawRect(x*150+150+10, y*150+150+10,80,80, 'blue')
      rect.touchUpInsideHandler = touch_handler
    timer += 1
    pytouch.update()

