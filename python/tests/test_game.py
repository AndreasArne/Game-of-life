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

    def assert_calc_bounds(self, type_of):
        """
        Asserts used to verify calc_bounds for both rows and columns
        """
        low_value = 0
        mid_value = 10
        top_value = 19
        out_below = -2
        out_above = 25

        index = game.calc_bounds(low_value, type_of)
        self.assertEqual(index, low_value)
        index = game.calc_bounds(mid_value, type_of)
        self.assertEqual(index, mid_value)
        index = game.calc_bounds(top_value, type_of)
        self.assertEqual(index, top_value)

        index = game.calc_bounds(out_below, type_of)
        self.assertEqual(index, 18)
        index = game.calc_bounds(out_above, type_of)
        self.assertEqual(index, 5)

        config.NR_ROWS = 10
        config.NR_COLS = 10

        index = game.calc_bounds(low_value, type_of)
        self.assertEqual(index, low_value)        
        index = game.calc_bounds(out_above, type_of)
        self.assertEqual(index, 5)
        index = game.calc_bounds(out_below, type_of)
        self.assertEqual(index, 8)

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

    def test_b1_calc_bounds_row(self):
        """
        Test function calc_bounds with rows
        """
        type_of = "r"
        self.assert_calc_bounds(type_of)

    def test_b2_calc_bounds_column(self):
        """
        Test function calc_bounds with columns
        """
        type_of = "c"
        self.assert_calc_bounds(type_of)



        # config.NR

    def assert_check_bounds_column(self):
        """
        Common asserts used for function check_bounds_column()
        """
        value = game.check_bounds_column(config.NR_COLS-1)
        self.assertTrue(value)
        value = game.check_bounds_column(config.NR_COLS)
        self.assertFalse(value)
        value = game.check_bounds_column(config.NR_COLS+1)
        self.assertFalse(value)

    def test_c1_check_bounds_column(self):
        """
        Test function check_bounds_column()
        """
        self.assert_check_bounds_column()

    def test_c2_check_bounds_column_change_config(self):
        """
        Test function check_bounds_column() with changed config value for NR_COLS
        """
        config.NR_COLS = 9
        self.assert_check_bounds_column()

    def test_d1_get_neighborhood(self):
        """
        Test function on a 10x10 gamefield
        """
        config.NR_COLS = 10
        config.NR_ROWS = 10
        gamefield = [
            [1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        # top left
        nh = game.get_neighborhood(gamefield, 0, 0)
        self.assertEqual(nh, 4)
        # top right
        nh = game.get_neighborhood(gamefield, 0, 8)
        self.assertEqual(nh, 2)
        # bottom left
        nh = game.get_neighborhood(gamefield, 9, 1)
        self.assertEqual(nh, 4)
        # bottom right
        nh = game.get_neighborhood(gamefield, 9, 9)
        self.assertEqual(nh, 4)
        # center
        nh = game.get_neighborhood(gamefield, 4, 5)
        self.assertEqual(nh, 3)

    def test_d2_get_neighborhood_small(self):
        """
        Test function with a small gamefield, 3x3
        """
        config.NR_COLS = 3
        config.NR_ROWS = 3
        gamefield = [
            [1, 0, 0],
            [1, 0, 0],
            [0, 1, 1],
        ]
        # top left
        nh = game.get_neighborhood(gamefield, 0, 0)
        self.assertEqual(nh, 3)
        # top right
        nh = game.get_neighborhood(gamefield, 0, 2)
        self.assertEqual(nh, 4)
        # bottom left
        nh = game.get_neighborhood(gamefield, 2, 0)
        self.assertEqual(nh, 4)
        # bottom right
        nh = game.get_neighborhood(gamefield, 2, 2)
        self.assertEqual(nh, 3)
        # center
        nh = game.get_neighborhood(gamefield, 1, 1)
        self.assertEqual(nh, 4)
    
    def test_e1_activate_rules(self):
        """
        Test activate_rules() on a 5x5 gamefield
        """
        pass


    # def tick


    # start
    # game_loop
    # prettyprint

if __name__ == '__main__':
    unittest.main(verbosity=2)
