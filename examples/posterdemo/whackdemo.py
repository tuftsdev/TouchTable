"""
    Whack-a-mole Application for TouchTable poster demo
"""
import os, sys, inspect
CUR_DIR = os.path.dirname(os.path.abspath(
                                    inspect.getfile(inspect.currentframe())))
PAR_DIR = os.path.dirname(CUR_DIR)
PAR_DIR = os.path.dirname(PAR_DIR)
sys.path.insert(0, PAR_DIR)

import pytouch
import random

class WhackApp(object):
    '''
    Docstring
    '''
    def __init__(self):
        self.score = 0
        self.running = False
        self.quit = None
        self.scoretext = None
        self.holes = []

    def exit(self, obj, touch):
        self.running = False

    def touch_handler(self, obj, touch):
        obj.change_image('mole_hit.png')
        self.score += 10
        self.scoretext.changeText("Score: " + str(self.score))

    def reset(self):
        pass

    def run(self, p):
        self.score = 0
        self.running = True
        self.scoretext = p.Text(0, 0,"Score: " + str(self.score), 30, z_index=1)
        self.quit = p.Text(0, 0, "QUIT", 60, z_index=1)
        self.quit.move(p.screen_w - self.quit.width, p.screen_h - self.quit.height)
        self.quit.touchUpInsideHandler = self.exit
        self.holes = []
        OFFSET_W = 0
        for i in range (1, 4):
            for j in range(1, 4):
                hole = p.Image("hole.png", 0, 0)
                OFFSET_W = (p.screen_w - hole.width * 3) / 4
                hole.move(j * OFFSET_W + (j-1) * hole.width, i * p.screen_h/4 - hole.height/2)
                self.holes.append(hole)
        x = random.randint(1, 3)
        y = random.randint(1, 3)
        mole = p.Image("mole_cartoon.png", 0, 0, z_index=5)
        mole.move(x * OFFSET_W + (x-1) * mole.width, y * p.screen_h/4 - mole.height/2)
        mole.touchUpInsideHandler = self.touch_handler

        timer = 0
        timer_max = random.randint(50,100)
        while self.running:
            if timer > timer_max:
                timer_max = random.randint(50,100)
                timer = 0
                x = random.randint(1, 3)
                y = random.randint(1, 3)
                mole.move(x * OFFSET_W + (x-1) * mole.width, y * p.screen_h/4 - mole.height/2)
            elif timer == 1:
                mole.change_image("mole_cartoon.png")
                mole.touchUpInsideHandler = self.touch_handler # ???
            timer += 1
            p.update()
        # Clean up
        mole.remove()
        mole = None
        for hole in self.holes:
            hole.remove()
        self.holes = []
        if self.scoretext is not None:
            self.scoretext.remove()
            self.scoretext = None
        if self.quit is not None:
            self.quit.remove()
            self.quit = None

if __name__ == "__main__":
    w = WhackApp()
    p = pytouch.init()
    w.run(p)
