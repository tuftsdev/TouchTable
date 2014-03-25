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
        i = 0
        for obj in self.objects:
            if obj.active:
                obj.update(obj)
            else:
                self.objects.pop(i)
            i += 1
        self.clear()
        self.redraw()
        self.sortObjects()
        pygame.display.flip()

    def redraw(self):
        for obj in reversed(self.objects):
            if obj.visible:
                obj.draw(self.screen)

    def Rect(self, x, y, width, height, z_index=0, drag_enabled=False, color='white', edge_thickness=0):
        newRect = pyobject.Rectangle(x, y, width, height, z_index, drag_enabled, color, edge_thickness)
        self.objects.append(newRect)
        return newRect

    def Circle(self, center, radius, z_index=0, drag_enabled=False, color='white', edge_thickness=0):
        newCircle = pyobject.Circle(center, radius, z_index, drag_enabled, color, edge_thickness)
        self.objects.append(newCircle)
        return newCircle

    def Image(self, image, x, y, z_index=0, drag_enabled=False):
        newImage = pyobject.Image(image, x, y, z_index, drag_enabled)
        self.objects.append(newImage)
        return newImage

    def Text(self, x, y, text, fontsize, fontcolor=(255,255,255), font=None, aa=1, z_index=0, drag_enabled=False):
        newText = pyobject.Text(x, y, text, fontsize, fontcolor, font, aa, z_index, drag_enabled)
        self.objects.append(newText)
        return newText

    def SpriteAnim(self, image, x, y, frame_x, frame_y, frame_width, frame_height, z_index=0, drag_enabled=False):
        newSprite = pyobject.SpriteAnim(image, x, y, frame_x, frame_y, frame_width, frame_height, z_index, drag_enabled)
        self.objects.append(newSprite)
        return newSprite

    def sortObjects(self):
        self.objects = sorted(self.objects, key=lambda obj: obj.z_index, reverse=True)

    def clear(self):
        self.screen.fill(self.bgcolor)
