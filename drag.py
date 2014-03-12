import pytouch
import random

def drag_handler(touch,self):
  self.move(touch.xpos - self.width/2, touch.ypos - self.height/2)

def hold_handler(touch,self):
  r = random.randint(0,255)
  g = random.randint(0,255)
  b = random.randint(0,255)
  self.changeColor(r,g,b,1)

if __name__ == "__main__":
  pytouch = pytouch.PyTouch()

  rect = pytouch.drawRect(300,300,50,50,'white')
  rect.dragHandler = drag_handler
  rect.holdHandler = hold_handler

  rect2 = pytouch.drawRect(400,400,60,100, 'blue',z_index=10)
  rect2.dragHandler = drag_handler
  rect2.holdHandler = hold_handler
  while 1:
    pytouch.update()
