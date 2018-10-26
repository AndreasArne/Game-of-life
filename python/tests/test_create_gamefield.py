#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Tests the functions used to create the gamefield used in Conway's game of life
"""
from sys import argv, path
import os
import unittest
path.insert(1, os.path.join(path[0], '..'))
from game import create_gamefield as cg
from game import config

class TestCreateGamefield(unittest.TestCase):
    """
    Test the different functions used for creating the gamefield in create_gamefield.py
    """

    def setUp(self):
        config.NR_COLS = 20
        config.NR_ROWS = 20
        config.PATTERN_PATH = "../patterns"

    def assert_structue_of_gamefield(self, gamefield):
        """
        Assert a gamefield created with random values.
        Used by multiple tests that should have same result
        """
        self.assertIsInstance(gamefield, type([]))
        self.assertEqual(len(gamefield), config.NR_ROWS)
        self.assertIsInstance(gamefield[0], type([]))
        self.assertEqual(len(gamefield[0]), config.NR_COLS)

    def test_a1_create_2dlist(self):
        """
        Testing creat_2dlist function
        """
        gamefield = cg.create_2dlist()
        self.assert_structue_of_gamefield(gamefield)

    def test_b1_random_startvalues(self):
        """
        Test creation of gamefield with random startvalue
        """
        gamefield = cg.random_startvalues()
        self.assert_structue_of_gamefield(gamefield)

    def test_b2_random_startvalues_fail(self):
        """
        Test creation of gamefield with random start values
        not having same number of rows and cols
        """
        config.NR_ROWS = 10
        with self.assertRaises(AssertionError):
            gamefield = cg.random_startvalues()

    def test_c1_get_pattern(self):
        """
        Test reading pattern from file
        """
        pattern = cg.get_pattern("beacon")
        self.assertEqual(pattern, [
            [0,0,0,0,0,0],
            [0,1,1,0,0,0],
            [0,1,0,0,0,0],
            [0,0,0,0,1,0],
            [0,0,0,1,1,0],
            [0,0,0,0,0,0],
        ])

    def test_c2_get_pattern_no_file(self):
        """
        Test reading pattern from file when file not exist
        """
        with self.assertRaises(FileNotFoundError):
            pattern = cg.get_pattern("no_such_file")

    def test_d1_inject_pattern_biggersize(self):
        """
        Test reading pattern from file,
        when gamefield is bigger than pattern
        """
        beacon = [
            [0,0,0,0,0,0],
            [0,1,1,0,0,0],
            [0,1,0,0,0,0],
            [0,0,0,0,1,0],
            [0,0,0,1,1,0],
            [0,0,0,0,0,0],
        ]
        config.NR_ROWS = 10
        config.NR_COLS = 10
        gamefield_pre = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        gamefield_pattern = cg.inject_pattern(gamefield_pre, beacon)
        self.assertEqual(gamefield_pattern, [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ])

    def test_d2_inject_pattern_samesize(self):
        """
        Test reading pattern from file when
        gamefield is same size as pattern
        """
        beacon = [
            [0,0,0,0,0,0],
            [0,1,1,0,0,0],
            [0,1,0,0,0,0],
            [0,0,0,0,1,0],
            [0,0,0,1,1,0],
            [0,0,0,0,0,0],
        ]
        config.NR_ROWS = len(beacon)
        config.NR_COLS = len(beacon[0])
        gamefield_pre = [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
        ]
        gamefield_pattern = cg.inject_pattern(gamefield_pre, beacon)
        self.assertEqual(gamefield_pattern, [
            [0, 0, 0, 0, 0, 0],
            [0, 1, 1, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 0, 1, 1, 0],
            [0, 0, 0, 0, 0, 0]
        ])

    def test_d3_inject_pattern_smallersize(self):
        """
        Test reading pattern from file when gamefield is smaller than pattern
        """
        beacon = [
            [0,0,0,0,0,0],
            [0,1,1,0,0,0],
            [0,1,0,0,0,0],
            [0,0,0,0,1,0],
            [0,0,0,1,1,0],
            [0,0,0,0,0,0],
        ]
        config.NR_ROWS = 5
        config.NR_COLS = 5
        gamefield_pre = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]
        gamefield_pattern = cg.inject_pattern(gamefield_pre, beacon)
        self.assertEqual(gamefield_pattern, [
            [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ])

    def test_e1_startvalues_fromfile_biggersize(self):
        """
        Test creating gamefield from file with pattern.
        When gamefield is bigger than pattern
        """
        config.NR_ROWS = 10
        config.NR_COLS = 10
        gamefield = cg.startvalues_fromfile("beacon")
        self.assertEqual(gamefield, [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ])

    def test_e2_startvalues_fromfile_samesize(self):
        """
        Test creating gamefield from file with pattern.
        When gamefield is same size as pattern.
        """
        config.NR_ROWS = 6 # len of beacon
        config.NR_COLS = 6 # len of beacon[0]
        gamefield = cg.startvalues_fromfile("beacon")
        self.assertEqual(gamefield, [
            [0, 0, 0, 0, 0, 0],
            [0, 1, 1, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 0, 1, 1, 0],
            [0, 0, 0, 0, 0, 0]
        ])

    def test_e3_startvalues_fromfile_smallersize(self):
        """
        Test creating gamefield from file with pattern.
        When gamefield is smaller
        """
        config.NR_ROWS = 5 # len of beacon is 6
        config.NR_COLS = 5 # len of beacon[0] is 6
        gamefield = cg.startvalues_fromfile("beacon")
        self.assertEqual(gamefield, [
            [0, 0, 0, 0, 0, 0],
            [0, 1, 1, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 0, 1, 1, 0],
            [0, 0, 0, 0, 0, 0]
        ])

    def test_e4_startvalues_fromfile_smalldiffsize(self):
        """
        Test creating gamefield from file with pattern.
        When gamefield is smaller and pattern size diff between
        rows and cols
        """
        config.NR_ROWS = 5 # len of beacon is 6
        config.NR_COLS = 5 # len of beacon[0] is 6
        with self.assertRaises(ValueError):
            gamefield = cg.startvalues_fromfile("beehive")

    def test_f5_startvalues_fromfile_no_file(self):
        """
        Test creating gamefield from file with pattern.
        When no such file exist
        """
        with self.assertRaises(FileNotFoundError):
            gamefield = cg.startvalues_fromfile("no_such_file")

    def test_f1_create_gamefield_random(self):
        """
        Test the create_gamefield() function without argv
        """
        gamefield = cg.create_gamefield()
        self.assert_structue_of_gamefield(gamefield)

    def test_f2_create_gamefield_file(self):
        """
        Test the create_gamefield() function with argv
        """
        config.NR_COLS = 10
        config.NR_ROWS = 10
        arg = "beehive"
        argv.append(arg)

        gamefield = cg.create_gamefield()
        self.assertEqual(gamefield, [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ])
        argv.remove(arg)


    def test_g1_check_argv_with(self):
        """
        Test the check_if_cmdinp() function with argv
        """
        arg = "beehive"
        argv.append(arg)

        filename = cg.check_if_cmdinp()
        self.assertEqual(filename, arg)
        argv.remove(arg)

    def test_g2_check_argv(self):
        """
        Test the check_If_cmdinp() function without argv
        """
        global argv
        old_argv = argv
        argv = argv[:1]
        filename = cg.check_if_cmdinp()
        self.assertEqual(filename, "")
        argv = old_argv

if __name__ == '__main__':
    unittest.main(verbosity=2)
