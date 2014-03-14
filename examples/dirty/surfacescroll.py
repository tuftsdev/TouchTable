import pygame
from pygame.locals import *

import sys


pygame.init()

image = pygame.image.load("pysnake150.png")
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Scroll test')
print type(screen)


base = pygame.Surface(screen.get_size()).convert()
base.fill((255,255,255))


subs = image.subsurface((0,0,500,500))
transparent = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
#image.convert_alpha()
#image.scroll(10,10)
screen.blit(base, (0,0))
transparent.blit(image,(0,0))
transparent.fill
transparent.set_alpha(255)
screen.blit(transparent,(0,0))
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

pygame.quit()
