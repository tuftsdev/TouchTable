import pytouch
import random


if __name__ == "__main__":
  pytouch = pytouch.PyTouch()

  def drag_handler(touch,self):
    pytouch.clear()
    pytouch.redraw(self)
    self.move(touch.xpos - self.width/2, touch.ypos - self.height/2)

  rect = pytouch.drawRect(300,300,50,50,'white')
  rect.dragHandler = drag_handler

  rect2 = pytouch.drawRect(400,400,60,100, 'blue')
  rect2.dragHandler = drag_handler
  while 1:
    pytouch.update()
