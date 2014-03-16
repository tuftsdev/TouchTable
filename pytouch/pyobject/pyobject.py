import pygame

class PyObject(object):
    def __init__(self, x, y, width, height, z_index=0,drag_enabled=False):
        if self.__class__ == PyObject:
            raise NotImplementedError('PyObject is abstract')

        self.x = x
        self.y = y
        self.z_index = z_index
        self.width = width
        self.height = height

        self.drag_enabled = drag_enabled

        self.rect = pygame.Rect(x, y, width, height)

    def draw(self):
        pass

    def move(self, x, y):
        self.rect = self.rect.move(x - self.x, y - self.y)
        self.x = x
        self.y = y

    def touchInside(self, touch):
        if(touch.xpos >= self.rect.left and touch.xpos <= self.rect.right and touch.ypos >= self.rect.top and touch.ypos <= self.rect.bottom):
            if touch.status == "dragging":
                self.dragHandler(self,touch)
            elif touch.status == "holding":
                self.holdHandler(self,touch)
            elif touch.status == "clicked":
                self.touchUpInsideHandler(self,touch)
            return True

    def dragHandler(self, obj, touch, extra=None):
        if self.drag_enabled:
            self.move(touch.xpos - self.width/2, touch.ypos - self.height/2)


    def holdHandler(self, obj, touch, extra=None):
        pass

    def touchUpInsideHandler(self, obj, touch, extra=None):
        pass
