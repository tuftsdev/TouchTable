import pytouch
import random

def drag_handler(self, touch):
  self.move(touch.xpos - self.width/2, touch.ypos - self.height/2)

def hold_handler(self, touch):
  r = random.randint(0,255)
  g = random.randint(0,255)
  b = random.randint(0,255)
  self.changeColor(r,g,b,1)

if __name__ == "__main__":
  pytouch = pytouch.PyTouch()
  
  rect = pytouch.drawRect(300,300,50,50,drag_enabled=True,color='white')
  rect.dragHandler = drag_handler
  rect.holdHandler = hold_handler
  
  rect2 = pytouch.drawRect(400,400,60,100,drag_enabled=True,color='blue')
  #rect2.dragHandler = drag_handler
  rect2.holdHandler = hold_handler

  image = pytouch.drawImage("pysnake.png", 50, 50)
  image.dragHandler = drag_handler
  image.convert()

  image = pytouch.drawImage("pysnake.png", 150, 150, drag_enabled=True)
  image.convert()

  text = pytouch.drawText(500, 500, "hello world!", 30, (255,255,255), drag_enabled=True)


  while 1:
    pytouch.update()
