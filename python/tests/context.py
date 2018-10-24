"""
Import all modules from ../game/ so test modules don't need to import path
"""
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from game import game
from game import create_gamefield
from game import turtle_gui
from game import config
