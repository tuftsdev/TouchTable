# 
# Pytouch - Python~TUIO toolkit
# 
# 

import sys

from distutils.core import setup

# Detect Python version
if sys.version > '3':
    PY3 = True
else:
    PY3 = False

# Determine System platform
platform = sys.platform

if sys.platform == 'darwin':
    if sys.maxsize > 2**32:
        osx_arch = 'x86_64'
    else:
        osx_arch = 'i386'

# Detect if Pygame is installed
have_pygame = False
try:
    from pygame.version import ver
    have_pygame = True
except ImportError:
    print('Pygame missing, it is required!\n')
    raise


# Setup
setup(
    name='Pytouch',
    version=pytouch.__version__,
    author='Andrew Li and Aaron Wishnick',
    author_email='...',
    url='...',
    license='...',
    descrition=(
        'A software library for touch table development '
        'with TUIO.'),
    #ext_modules=ext_modules, # WILL NEED THESE EXT. MODULES
    packages=[
        'pytouch',
        'pytouch.input',
        'pytouch.input.providers'],
    package_dir={'pytouch': 'pytouch'}
)