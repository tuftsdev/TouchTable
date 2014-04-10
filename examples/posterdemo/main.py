"""
    Application launcher for TouchTable poster demo
"""
import os, sys, inspect
from whackdemo import WhackApp
from pixeldemo import PixelApp

CUR_DIR = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
PAR_DIR = os.path.dirname(CUR_DIR)
PAR_DIR = os.path.dirname(PAR_DIR)
sys.path.insert(0, PAR_DIR)

import pytouch
import random

STAR_SPAWN_Y = -4
STAR_WIDTH = 4
STAR_HEIGHT = 4
STAR_SPEED = 1
STAR_POPULATE_CHANCE = 99
STAR_SPAWN_CHANCE = 75
STAR_POPULATE_SPACING = 8
class PixelBackground():
    def __init__(self, pytouch):
        self.starfield = PixelBackground.Starfield(pytouch)
        self.pytouch = pytouch
        self.ship = pytouch.Image("ship.png", 3 * pytouch.screen_w/4 - 25, pytouch.screen_h - 100, z_index=3)

    def update(self):
        self.starfield.update()

    def clean(self):
        self.ship.remove()
        self.ship = None
        self.starfield.clean()

    class Star():
        def __init__(self, pytouch, x, y=STAR_SPAWN_Y):
            self.obj = pytouch.Rect(x, y, STAR_WIDTH, STAR_HEIGHT, color='white', alpha=random.randint(50,255))
            self.obj.update = self.update
            self.active = True

        def update(self, obj):
            obj.move(obj.x, obj.y + STAR_SPEED)

    class Starfield():
        def __init__(self, pytouch):
            self.stars = []
            self.pytouch = pytouch
            self.populate()

        def populate(self):
            i = 0
            while i < self.pytouch.screen_h:
                j = self.pytouch.screen_w/2 + 4
                while j < self.pytouch.screen_w:
                    if random.randint(0,100) > STAR_POPULATE_CHANCE:
                        newStar = PixelBackground.Star(self.pytouch, j, i)
                        self.stars.append(newStar)
                    j += STAR_POPULATE_SPACING
                i += STAR_POPULATE_SPACING

        def update(self):
        # Attempt to spawn a star
            if random.randint(0,100) > STAR_SPAWN_CHANCE:
                spawn = True
                newStar = PixelBackground.Star(self.pytouch, random.randint(self.pytouch.screen_w/2 + 4, self.pytouch.screen_w-4))
                for star in self.stars: # TODO DON'T NEED THIS
                    if star.obj.collide(newStar.obj):
                        spawn = False
                        break
                if spawn:
                    self.stars.append(newStar)
                else:
                    newStar.obj.remove()
            i = 0
            for star in self.stars:
                if star.obj.y > self.pytouch.screen_h + 4:
                    star.obj.remove()
                    self.stars.pop(i)
                    i -= 1
                i += 1
                
        def clean(self):
            for star in self.stars:
                star.obj.remove()
            self.stars = []

class WhackBackground():
    def __init__(self, pytouch):
        self.pytouch = pytouch
        
        self.hole = self.pytouch.Image("hole.png", 0, 0)
        self.hole.move(self.pytouch.screen_w/4 - self.hole.rect.width/2, self.pytouch.screen_h - self.hole.rect.height)
        self.mole = self.pytouch.Image("mole_cartoon.png", 0, 0)
        self.mole.move(self.pytouch.screen_w/4 - self.mole.rect.width/2, self.pytouch.screen_h - self.mole.rect.height)
        self.timer = 0
        self.timer_max = 200

    def update(self):
        if self.timer > self.timer_max:
            self.timer = 0
            self.mole.setVisible(not self.mole.visible) # hack to get visibility
        else:
            self.timer += 1


    def clean(self):
        self.hole.remove()
        self.hole = None
        self.mole.remove()
        self.mole = None


class App(object):
    """
    Docstring
    """
    def __init__(self):
        random.seed()
        self.pytouch = pytouch.init()

        self.whack = WhackApp()
        self.pixel = PixelApp()

        self.running = True

        #self.whack_launcher = self.pytouch.Rect(100, 100, 300, 100, z_index=1)
        self.whack_launcher = self.pytouch.Text(0, 0, "Whack-A-Mole", 60, z_index=3)
        self.whack_launcher.move(self.pytouch.screen_w/4 - self.whack_launcher.rect.width/2, self.pytouch.screen_h/2 - self.whack_launcher.rect.height/2)
        self.whack_launcher.touchUpInsideHandler = self.launch_whack
        #self.pixel_launcher = self.pytouch.Rect(500, 100, 300, 100, z_index=1)
        self.pixel_launcher = self.pytouch.Text(0, 0, "Pixel Shooter", 60, z_index=3)
        self.pixel_launcher.move(3 * self.pytouch.screen_w/4 - self.pixel_launcher.rect.width/2, self.pytouch.screen_h/2 - self.pixel_launcher.rect.height/2)
        self.pixel_launcher.touchUpInsideHandler = self.launch_pixel

        self.quit = self.pytouch.Text(self.pytouch.screen_w-120, 0, "QUIT", 60, z_index=1)
        self.quit.touchUpInsideHandler = self.exit

    def exit(self, obj, touch):
        self.running = False

    def run(self):
        self.pb = PixelBackground(self.pytouch)
        self.wb = WhackBackground(self.pytouch)
        while self.running:
            self.pb.update()
            self.wb.update()
            self.pytouch.update()

    def launch_whack(self, obj,touch):
        self.whack_launcher.setVisible(False)
        self.pixel_launcher.setVisible(False)
        self.quit.setVisible(False)

        self.wb.clean()
        self.wb = None
        self.pb.clean()
        self.pb = None

        self.whack.run(self.pytouch)

        self.pb = PixelBackground(self.pytouch)
        self.wb = WhackBackground(self.pytouch)

        self.whack_launcher.setVisible(True)
        self.pixel_launcher.setVisible(True)
        self.quit.setVisible(True)

    def launch_pixel(self, obj,touch):
        self.whack_launcher.setVisible(False)
        self.pixel_launcher.setVisible(False)
        self.quit.setVisible(False)

        self.wb.clean()
        self.wb = None
        self.pb.clean()
        self.pb = None

        self.pixel.run(self.pytouch)

        self.pb = PixelBackground(self.pytouch)
        self.wb = WhackBackground(self.pytouch)

        self.whack_launcher.setVisible(True)
        self.pixel_launcher.setVisible(True)
        self.quit.setVisible(True)

if __name__ == "__main__":
    app = App()
    app.run()
