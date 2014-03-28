import pytouch
import random

score = 0
scoretext = None

def touch_handler(obj, touch):
  obj.changeColor('red')
  global score
  global scoretext
  score += 10
  scoretext.changeText("Score: " + str(score))

if __name__ == "__main__":
  pytouch = pytouch.PyTouch()
  scoretext = pytouch.Text(0, 0, "Score: " + str(score), 30, z_index = 1)
  timer = 0
  for i in range(0, 3):
    for j in range(0, 3):
      pytouch.Rect(j*150+150, i*150+150, 100,100)
  x = random.randint(0,2)
  y = random.randint(0,2)
  rect = pytouch.Rect(x*150+150+10, y*150+150+10,80,80, 'blue')
  rect.touchUpInsideHandler = touch_handler

  timer_max = random.randint(50,100)
  while 1:
    if timer > timer_max:
      timer_max = random.randint(50,100)
      timer = 0
      x = random.randint(0,2)
      y = random.randint(0,2)
      rect.move(x*150+160, y*150+160)
    elif timer == 1:
      rect.changeColor('blue')
    timer += 1
    pytouch.update()
