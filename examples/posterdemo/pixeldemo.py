"""
    Pixel Shooter Application for TouchTable poster demo
"""
import os, sys, inspect
CUR_DIR = os.path.dirname(os.path.abspath(
                                    inspect.getfile(inspect.currentframe())))
PAR_DIR = os.path.dirname(CUR_DIR)
PAR_DIR = os.path.dirname(PAR_DIR)
sys.path.insert(0, PAR_DIR)

import pytouch

class PixelApp(object):
    def __init__(self):
        pass
        