import kivy
kivy.require('1.1.1')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, NumericProperty

from kivy.clock import Clock

from kivy.config import Config
import random

class WhackMole(Widget):
    up = False
    hit = False

    def reset(self):
        self.up = True

    def whacked(self):
        print("WHACKED")
        self.hit = True

    def on_touch_down(self, touch):
        if (self.up):
            if (touch.x < self.x + 80) and (touch.x > self.x) and (touch.y < self.y + 80) and (touch.y > self.y):
                self.whacked()

    def toggle(self, dt=None):
        self.up = not self.up
        if not self.up:
          self.opacity = 0
        else:
          self.opacity = 1

class Hole(Widget):
    def draw_mole(self, mole):
        mole.center = self.center

class WhackGame(Widget):
    mole = ObjectProperty(None)
    score = NumericProperty(0)
    holes = []
    hole_1 = ObjectProperty(None)
    hole_2 = ObjectProperty(None)
    hole_3 = ObjectProperty(None)
    hole_4 = ObjectProperty(None)
    hole_5 = ObjectProperty(None)
    hole_6 = ObjectProperty(None)
    hole_7 = ObjectProperty(None)
    hole_8 = ObjectProperty(None)
    hole_9 = ObjectProperty(None)
    hole_10 = ObjectProperty(None)
    hole_11 = ObjectProperty(None)
    hole_12 = ObjectProperty(None)
    hole_13 = ObjectProperty(None)
    hole_14 = ObjectProperty(None)
    hole_15 = ObjectProperty(None)

    def start(self):
        self.holes = [self.hole_1, self.hole_2, self.hole_3, self.hole_4, self.hole_5,
                      self.hole_6, self.hole_7, self.hole_8, self.hole_9, self.hole_10,
                      self.hole_11, self.hole_12, self.hole_13, self.hole_14, self.hole_15]
        self.move_mole()
        Clock.schedule_once(self.toggle, random.uniform(1, 3))
        # Clock.schedule_interval(self.toggle, 2)

    def update(self, dt):
        self.mole.v = dt
        if self.mole.hit:
          self.score += 1
          self.toggle()
          self.mole.hit = False

    def move_mole(self):
        hole_num = random.randint(0, len(self.holes)-1)
        hole = self.holes[hole_num]
        hole.draw_mole(self.mole)

    def toggle(self, dt=None):
        self.mole.toggle()
        if not self.mole.up:
          self.move_mole()
        Clock.schedule_once(self.toggle, random.uniform(1, 3))
class WhackApp(App):
    def build(self):
    # Initialize TUIO
        Config.set('input','multithouchscreen1','tuio,127.0.0.1:3333')

        game = WhackGame()
        game.start()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game

if __name__ == '__main__':
    WhackApp().run()
