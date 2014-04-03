import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
parentdir = os.path.dirname(parentdir)
sys.path.insert(0,parentdir) 

import pytouch
import random

score = 0
scoretext = None
SCREEN_W = 0
SCREEN_H = 0
RESIZE = False
run = True

def touch_handler(obj, touch):
  global score, scoretext, SCREEN_W, SCREEN_H, RESIZE
  if obj.enabled:
    obj.enabled = False
    obj.change_image(os.path.join(os.path.dirname(__file__),'mole_hit.png'))
    if RESIZE:
      obj.resize(SCREEN_W/5,SCREEN_H/5)
    score += 10
    scoretext.changeText("Score: " + str(score))

def run(external=False, p=None):
  global SCREEN_W, SCREEN_H, scoretext, RESIZE, score, run
  if p is not None:
    pyt = p
  else:
    pyt = pytouch.init()
  SCREEN_W = pyt.screen_w
  SCREEN_H = pyt.screen_h
  OFFSET_W = SCREEN_W/8
  OFFSET_H = SCREEN_H/8
  scoretext = pyt.Text(0, 0, "Score: " + str(score), 30, z_index = 1)
  timer = 0
  for i in range(0, 3):
    for j in range(0, 3):
      hole = pyt.Image(os.path.join(os.path.dirname(__file__),"hole.png"), j*SCREEN_W/5+j*OFFSET_W, i*SCREEN_H/5+i*OFFSET_H)
      if SCREEN_W/hole.image_rect.width < 5:
        RESIZE = True
        hole.resize(SCREEN_W/5, SCREEN_H/5)
  x = random.randint(0,2)
  y = random.randint(0,2)
  mole = pyt.Image(os.path.join(os.path.dirname(__file__),"mole_cartoon.png"), x*SCREEN_W/5+x*OFFSET_W, y*SCREEN_H/5+y*OFFSET_H, z_index = 5)
  if RESIZE:
    mole.resize(SCREEN_W/5, SCREEN_H/5)
  mole.touchUpInsideHandler = touch_handler

  timer_max = random.randint(50,100)
  while run:
    if timer > timer_max:
      timer_max = random.randint(50,100)
      timer = 0
      x = random.randint(0,2)
      y = random.randint(0,2)
      mole.move(x*SCREEN_W/5+x*OFFSET_W, y*SCREEN_H/5+y*OFFSET_H)
    elif timer == 1:
      mole.change_image(os.path.join(os.path.dirname(__file__),'mole_cartoon.png'))
      if RESIZE:
        mole.resize(SCREEN_W/5, SCREEN_H/5)
      mole.enabled = True
      mole.touchUpInsideHandler = touch_handler
    timer += 1
    pyt.update()

if __name__ == "__main__":
    run()
