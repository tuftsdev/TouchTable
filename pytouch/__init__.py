
__all__ = (
    'init',
    'Clock')

__version__ = '0.0.1'

import sys
from pytouch.time import Clock

clock = None

def init():
    pygame.init()
    clock = pytouch.time.Clock(pygame.time.Clock())

def Clock():
    if clock = None:
        # TODO: Convert to Logger, remove exit
        # ERROR NOT INITIALIZED
        sys.exit('ERROR: Pytouch not initialized')
    else:
        return clock
