"""
    Pixel Shooter Application for TouchTable poster demo
"""
import os, sys, inspect
import random
CUR_DIR = os.path.dirname(os.path.abspath(
                                    inspect.getfile(inspect.currentframe())))
PAR_DIR = os.path.dirname(CUR_DIR)
PAR_DIR = os.path.dirname(PAR_DIR)
sys.path.insert(0, PAR_DIR)

import pytouch

class PixelApp(object):
    def __init__(self):
        self.screen_w = 0
        self.screen_h = 0
        self.gameover = None
        self.p = None
        self.title = None
        self.title2 = None
        self.ship = None
        self.enemies = []
        self.stars = []
        self.score = 0
        self.scoretext = None
        self.titleWaiting = False
        self.running = False
        self.gameOverWaiting = False
        random.seed()

    def run(self, p):
        self.p = p
        self.p.touchedBackgroundHandler = self.touchedBackground
        self.screen_w = p.screen_w
        self.screen_h = p.screen_h

        self.gameover = p.Text(0, 0, "GAME OVER", 60, z_index = 3)
        self.gameover.setVisible(False)
        self.gameover.move(self.screen_w/2 - self.gameover.rect.width/2, self.screen_h/2 - self.gameover.rect.height/2)

        self.title = p.Text(0,0, "PIXEL SHOOTER", 60, z_index = 3)
        self.title.setVisible(False)
        self.title.move(self.screen_w/2 - self.title.rect.width/2, self.screen_h/2 - self.title.rect.height/2)

        self.title2 = p.Text(0,0, "Tap to Begin", 15, z_index = 3)
        self.title2.setVisible(False)
        self.title2.move(self.screen_w/2 - self.title2.rect.width/2, self.screen_h/2+50 - self.title2.rect.height/2)

        self.star_populate()

        self.titlePage()
        self.gamePlay()
        self.gameoverPage()

    def touchedBackground(self):
        if self.titleWaiting:
            self.titleWaiting = False
        elif self.gameOverWaiting:
            self.gameOverWaiting = False
            self.gamePlay()

    def titlePage(self):
        self.titleWaiting = True
        self.title.setVisible(True)
        self.title2.setVisible(True)
        while self.titleWaiting:
            self.star_update()
            self.p.update()
        self.title.setVisible(False)
        self.title2.setVisible(False)

    def gamePlay(self):
        self.running = True

    def gameoverPage(self):
        self.gameover.setVisible(True)
        while True:
            self.p.update()

    def star_populate(self):
        i = -16
        j = 0
        while i < self.screen_h:
            j = 0
            while j < self.screen_w:
                if random.randint(0, 100) > 99:
                    newStar = self.Star(self.p,j, i)
                    self.stars.append(newStar)
                j += 8
            i += 8

    def star_update(self):
        if random.randint(0, 100) > 75:
            spawn = True
            newStar = self.Star(self.p,random.randint(0, self.screen_w-4))
            for star in self.stars:
                if star.obj.collide(newStar.obj):
                    spawn = False
                    break
                if spawn:
                    self.stars.append(newStar)
                else:
                    newStar.obj.remove()

        i = 0
        for star in self.stars:
            if star.obj.y > self.screen_h + 4:
                star.obj.remove()
                self.stars.pop(i)
                i -= 1
            i += 1

    class Star():
        def __init__(self, p, x, y=-4):
            self.WIDTH = 4
            self.HEIGHT = 4
            self.obj = p.Rect(x, y, self.WIDTH, self.HEIGHT, color='white', alpha=random.randint(50,255))
            self.obj.update = self.update
            self.active = True

        def update(self, obj):
            obj.move(obj.x, obj.y + 1)




