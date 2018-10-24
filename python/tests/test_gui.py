#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Tests the functions used to for the gui in turtle_gui.py.
"""
from sys import argv, path
import os
import unittest

from context import turtle_gui
from context import config

class TestGui(unittest.TestCase):
    """
    Test the different functions used for in turtle_gui.py
    """

    def setUp(self):
        config.NR_COLS = 20
        config.NR_ROWS = 20

    def assert_calc_bounds(self, type_of):
        """
        Asserts used to verify calc_bounds for both rows and columns
        """
        pass

if __name__ == '__main__':
    unittest.main(verbosity=2)
