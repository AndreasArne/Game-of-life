#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Tests the functions used to calculate Conway's game of life in game.py
"""
from sys import argv, path
import os
import unittest
path.insert(1, os.path.join(path[0], '..'))
import game
import config

class TestGame(unittest.TestCase):
    """
    Test the different functions used for in game.py
    """

    def setUp(self):
        config.NR_COLS = 20
        config.NR_ROWS = 20
        config.PATTERN_PATH = "../patterns"
    
    def test_a1_check_rules(self):
        """
        Test function check_rules with different values
        """
        # Has rule
        rule = game.check_rules(1, 1)
        self.assertEqual(rule, 1)
        rule = game.check_rules(1, 2)
        self.assertEqual(rule, -1)
        rule = game.check_rules(1, 4)
        self.assertEqual(rule, 3)
        rule = game.check_rules(0, 3)
        self.assertEqual(rule, 4)
        rule = game.check_rules(1, 8)
        self.assertEqual(rule, 3)
        rule = game.check_rules(1, 0)
        self.assertEqual(rule, 1)

        # No rule match
        rule = game.check_rules(0, 1)
        self.assertEqual(rule, -1)
        rule = game.check_rules(0, 0)
        self.assertEqual(rule, -1)
        with self.assertRaises(ValueError):
            rule = game.check_rules(1, -1)
        with self.assertRaises(ValueError):
            rule = game.check_rules(1, 9)


    # def calc_bounds
    # def check_bounds_column
    # def get_neighborhood
    # def activate_rules
    # def tick


    # start
    # game_loop
    # prettyprint

if __name__ == '__main__':
    unittest.main(verbosity=2)
