import pytouch
import random

def touch_handler(touch, self):
  self.changeColor('white')

if __name__ == "__main__":
  pytouch = pytouch.PyTouch()
  timer = 0
  for i in range(0, 3):
    for j in range(0, 3):
      pytouch.drawRect(j*150+150, i*150+150, 100,100)
  x = random.randint(0,2)
  y = random.randint(0,2)
  rect = pytouch.drawRect(x*150+150+10, y*150+150+10,80,80, 'blue')
  rect.touchUpInsideHandler = touch_handler

  timer_max = random.randint(50,100)
  while 1:
    if timer > timer_max:
      timer_max = random.randint(50,100)
      pytouch.clear()
      for i in range(0, 3):
        for j in range(0, 3):
          pytouch.drawRect(j*150+150, i*150+150, 100,100)
      timer = 0
      x = random.randint(0,2)
      y = random.randint(0,2)
      rect = pytouch.drawRect(x*150+150+10, y*150+150+10,80,80, 'blue')
      rect.touchUpInsideHandler = touch_handler
    timer += 1
    pytouch.update()
