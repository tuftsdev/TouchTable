import pygame


class PyObject(object):
    '''
PyObject: Base class for all PyTouch objects.

Variables
=========
    x: [int] x position of top-left corner
    y: [int] y position of top-left corner
    z_index: [int] order of elements on the screen. Higher-numbered
             objects are positioned above lower-numbered objects.
    width: [int] width (x) of the object
    height: [int] height (y) of the object
    rect: [pygame.Rect] Pygame object which stores an object's
          rectangular coordinates, used in drawing rectangular objects
          and determining object collisions
    drag_enabled: [bool] defaults to False. If true, uses the default
                  dragHandler

Methods
=======
    draw(): Must be implemented in child classes
    update(): Can be implemented by user. Additional function called
              during each PyTouch.update() call which can perform some
              action on the object
    move(x, y): Moves object to a given x,y location (top-left corner)
    setVisible(visible): Sets visibility to given boolean
    touchInside(touch): Given a touch/click event, checks if it is
                        relevant to the object (inside) and calls the
                        appropriate handler
        dragHandler(obj, touch) => handles "dragging" events, defaults
                                   to moving the center of the object to
                                   the cursor
        holdHandler(obj, touch) => handles "holding" events, undefined
                                   by default
        touchUpInsideHandler(obj, touch) => handles "clicked" events,
                                            undefined by default
    collide(obj): Checks collision of self and given object's rects.
                  Object must have a rect (type pygame.Rect)
    collidelist(objlist): Checks collision of self and list of objects.
                          Returns index of first object which collides
                          with self, else returns -1.
    collidelistall(objlist): Checks collision of self and list of objects,
                             Returns a list of all indices which collides
                             with self, else returns an empty list.
    '''
    def __init__(self, x, y, width, height, z_index=0, drag_enabled=False):
        if self.__class__ == PyObject:
            raise NotImplementedError('PyObject is abstract')
        self.x = x
        self.y = y
        self.z_index = z_index
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)
        self.drag_enabled = drag_enabled
        self.visible = True
        self.active = True

    def draw(self):
        pass

    def update(self, obj):
        pass

    def move(self, x, y):
        self.rect = self.rect.move(x - self.x, y - self.y)
        self.x = x
        self.y = y

    def setVisible(self, visible):
        self.visible = visible

    def remove(self):
        self.active = False

    # EVENT HANDLING
    # ==============
    def touchInside(self, touch):
        if touch.xpos >= self.rect.left and touch.xpos <= self.rect.right and \
           touch.ypos >= self.rect.top and touch.ypos <= self.rect.bottom:
            if touch.status == "dragging":
                self.dragHandler(self, touch)
            elif touch.status == "holding":
                self.holdHandler(self, touch)
            elif touch.status == "clicked":
                self.touchUpInsideHandler(self, touch)
            return True

    def dragHandler(self, obj, touch, extra=None):
        if self.drag_enabled:
            self.move(touch.xpos - self.width/2, touch.ypos - self.height/2)

    def holdHandler(self, obj, touch, extra=None):
        pass

    def touchUpInsideHandler(self, obj, touch, extra=None):
        pass

    # OBJECT COLLISION
    # ================
    def collide(self, obj):
        return self.rect.colliderect(obj.rect)

    def collidelist(self, objList):
        return self.rect.collidelist(objList)

    def collidelistall(self, objList):
        return self.rect.collidelistall(objList)
