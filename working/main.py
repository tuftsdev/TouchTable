import pygame, touch
from pygame.locals import *

if __name__ == "__main__":
  pygame.init()
  screen = pygame.display.set_mode((800,600))
  touchTracker = touch.TouchTracker(800,600)
  while 1:
    touchTracker.update()

