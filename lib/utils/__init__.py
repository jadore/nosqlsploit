import os
import sys

try:
    __file__
except NameError:
    __file__ = sys.argv[0]

util_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(util_dir)
