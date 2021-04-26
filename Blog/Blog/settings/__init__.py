from .base import *

try:
    from .local import *
except ImportError:
    print('Cannot find module settings local! Make it from local.py skeleton')