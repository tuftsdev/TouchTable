import pytouch
import random

score = 0
scoretext = None
SCREEN_W = 0
SCREEN_H = 0
RESIZE = False

def touch_handler(obj, touch):
  global score, scoretex, SCREEN_W, SCREEN_H, RESIZE
  if obj.enabled:
    obj.enabled = False
    obj.change_image('mole_hit.png')
    if RESIZE:
      obj.resize(SCREEN_W/5,SCREEN_H/5)
    score += 10
    scoretext.changeText("Score: " + str(score))

if __name__ == "__main__":
  pytouch = pytouch.PyTouch()
  SCREEN_W = pytouch.screen_w
  SCREEN_H = pytouch.screen_h
  OFFSET_W = SCREEN_W/8
  OFFSET_H = SCREEN_H/8
  scoretext = pytouch.Text(0, 0, "Score: " + str(score), 30, z_index = 1)
  timer = 0
  for i in range(0, 3):
    for j in range(0, 3):
      hole = pytouch.Image("hole.png", j*SCREEN_W/5+j*OFFSET_W, i*SCREEN_H/5+i*OFFSET_H)
      if SCREEN_W/hole.image_rect.width < 5:
        RESIZE = True
        hole.resize(SCREEN_W/5, SCREEN_H/5)
  x = random.randint(0,2)
  y = random.randint(0,2)
  mole = pytouch.Image("mole_cartoon.png", x*SCREEN_W/5+x*OFFSET_W, y*SCREEN_H/5+y*OFFSET_H, z_index = 5)
  if RESIZE:
    mole.resize(SCREEN_W/5, SCREEN_H/5)
  mole.touchUpInsideHandler = touch_handler

  timer_max = random.randint(50,100)
  while 1:
    if timer > timer_max:
      timer_max = random.randint(50,100)
      timer = 0
      x = random.randint(0,2)
      y = random.randint(0,2)
      mole.move(x*SCREEN_W/5+x*OFFSET_W, y*SCREEN_H/5+y*OFFSET_H)
    elif timer == 1:
      mole.change_image('mole_cartoon.png')
      if RESIZE:
        mole.resize(SCREEN_W/5, SCREEN_H/5)
      mole.enabled = True
      mole.touchUpInsideHandler = touch_handler
    timer += 1
    pytouch.update()
