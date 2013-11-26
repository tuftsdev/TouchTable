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

class WhackGame(Widget):
    mole = ObjectProperty(None)
    score = NumericProperty(0)

    def start(self):
        #self.mole = WhackMole(size=(50,50))
        self.mole.center = self.center
        self.mole.reset()
        Clock.schedule_interval(self.toggle, 2)

    def update(self, dt):
        self.mole.v = dt
        if self.mole.hit:
          self.score += 1
          self.toggle()
          self.mole.hit = False

    def toggle(self, dt=None):
        self.mole.toggle()
        if not self.mole.up:
          self.mole.x = random.randint(0, self.width)
          self.mole.y = random.randint(0, self.height)

    # def on_touch_down(self, touch):
    #     #print ("Touch at x:%d y:%d" % (touch.x, touch.y))
    #     #print ("Compared to x:%d y:%d x+40:%d y+40:%d x-40:%d y-40:%d" % (self.mole.x, self.mole.y,self.mole.x + 40, self.mole.y + 40, self.mole.x - 40, self.mole.y-40))
    #     if (touch.x < self.mole.x + 80) and (touch.x > self.mole.x) and (touch.y < self.mole.y + 80) and (touch.y > self.mole.y):
    #         self.mole.whacked()

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
