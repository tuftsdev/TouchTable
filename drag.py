import pytouch
import random


if __name__ == "__main__":
  pytouch = pytouch.PyTouch()

  def drag_handler(touch,self):
    pytouch.clear()
    self.move(touch.xpos - self.width/2, touch.ypos - self.height/2)

  rect = pytouch.drawRect(300,300,50,50,'white')
  rect.dragHandler = drag_handler
  while 1:
    pytouch.update()
