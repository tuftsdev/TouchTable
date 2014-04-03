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

class App(object):
    """
    Docstring
    """
    def __init__(self):
        self.pytouch = pytouch.init()

        self.whack = WhackApp()
        self.pixel = PixelApp()

        self.running = True

        self.whack_launcher = self.pytouch.Rect(100, 100, 300, 100, z_index=1)
        self.whack_launcher.touchUpInsideHandler = self.launch_whack
        self.pixel_launcher = self.pytouch.Rect(500, 100, 300, 100, z_index=1)
        self.pixel_launcher.touchUpInsideHandler = self.launch_pixel

        self.quit = self.pytouch.Text(self.pytouch.screen_w-120, 0, "QUIT", 60, z_index=1)
        self.quit.touchUpInsideHandler = self.exit

    def exit(self, obj, touch):
        self.running = False

    def run(self):
        while self.running:
            self.pytouch.update()

    def launch_whack(self, obj,touch):
        self.whack_launcher.setVisible(False)
        self.pixel_launcher.setVisible(False)
        self.quit.setVisible(False)
        self.whack.run(self.pytouch)
        self.whack_launcher.setVisible(True)
        self.pixel_launcher.setVisible(True)
        self.quit.setVisible(True)

    def launch_pixel(self, obj,touch):
        self.whack_launcher.setVisible(False)
        self.pixel_launcher.setVisible(False)
        self.quit.setVisible(False)
        self.pixel.run(self.pytouch)
        self.whack_launcher.setVisible(True)
        self.pixel_launcher.setVisible(True)
        self.quit.setVisible(True)

if __name__ == "__main__":
    app = App()
    app.run()