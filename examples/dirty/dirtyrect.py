import pygame
from pygame.locals import *
import sys


class App():

    FPS = 30
    SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH,self.SCREEN_HEIGHT))
        pygame.display.set_caption('Dirty Rect Test')

        self.base = pygame.Surface(self.screen.get_size()).convert()
        self.base.fill((0,0,0))

        self.clock = pygame.time.Clock()

        self.isRunning = True

        self.dirty = []

        try:
            self.image = pygame.image.load("pysnake150.png")
        except:
            print("Failed to load image")

        self.image = self.image.convert_alpha()
        self.image_rect = self.image.get_rect()
        print self.image_rect
        print "width: ", self.image_rect.width
        print "height: ", self.image_rect.height
        self.image_x = 50
        self.image_y = 50


        self.screen.blit(self.base, (0,0))
        self.screen.blit(self.image, (self.image_x, self.image_y))
        pygame.display.flip()

    def run(self):
        while(self.isRunning):
            self.update()
            self.draw()
            self.clock.tick(self.FPS)

    def update(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_UP:
                    self.dirty.append(pygame.Rect(self.image_x, self.image_y, 
                                                  self.image_rect.width, self.image_rect.height))
                    self.image_y = self.image_y - 50
                elif event.key == pygame.K_DOWN:
                    self.dirty.append(pygame.Rect(self.image_x, self.image_y, 
                                                  self.image_rect.width, self.image_rect.height))
                    self.image_y = self.image_y + 50
                elif event.key == pygame.K_LEFT:
                    self.dirty.append(pygame.Rect(self.image_x, self.image_y, 
                                                  self.image_rect.width, self.image_rect.height))
                    self.image_x = self.image_x - 50
                elif event.key == pygame.K_RIGHT:
                    self.dirty.append(pygame.Rect(self.image_x, self.image_y, 
                                                  self.image_rect.width, self.image_rect.height))
                    self.image_x = self.image_y + 50
        
        self.screen.blit(self.base, (0,0))
        self.screen.blit(self.image, (self.image_x, self.image_y))
        pygame.display.update(self.dirty)
        self.dirty = []


                

    def draw(self):
        if self.dirty:
            pygame.display.update(pygame.Rect(0,0,50,50))


if __name__ == '__main__':
    a = App()
    a.run()

