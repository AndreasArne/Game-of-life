#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Tests the implementation of Conway's game of life
"""
import unittest
import game

class TestGamefield(unittest.TestCase):
    """
    Test for creating gamefield in game.py
    """
    def setup(self):
        game.NR_COLS = 20
        game.NR_ROWS = 20

    def test_a1_create_random(self):
        """
        Test creation of gamefield with random startvalue
        """
        gamefield = game.random_startvalues()
        self.assertIsInstance(gamefield, type([]))
        self.assertEqual(len(gamefield), game.NR_ROWS)
        self.assertIsInstance(gamefield[0], type([]))
        self.assertEqual(len(gamefield[0]), game.NR_COLS)

    def test_a2_create_random_fail(self):
        """
        Test creation of gamefield with random start values
        not having same nr_rows and cols
        """
        game.NR_ROWS = 10
        with self.assertRaises(AssertionError):
            gamefield = game.random_startvalues()

    def test_b1_get_pattern(self):
        """
        Test reading pattern from file
        """
        pattern = game.get_pattern("beacon")
        self.assertEqual(pattern, [
            [0,0,0,0,0,0],
            [0,1,1,0,0,0],
            [0,1,0,0,0,0],
            [0,0,0,0,1,0],
            [0,0,0,1,1,0],
            [0,0,0,0,0,0],
        ])

    def test_b2_get_pattern_no_file(self):
        """
        Test reading pattern from file when file not exist
        """
        with self.assertRaises(FileNotFoundError):
            pattern = game.get_pattern("no_such_file")

    def test_c1_inject_pattern_biggersize(self):
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
        game.NR_ROWS = 10
        game.NR_COLS = 10
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
        gamefield_pattern = game.insert_pattern(gamefield_pre, beacon)
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

    def test_c2_inject_pattern_samesize(self):
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
        game.NR_ROWS = len(beacon)
        game.NR_COLS = len(beacon[0])
        gamefield_pre = [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
        ]
        gamefield_pattern = game.insert_pattern(gamefield_pre, beacon)
        self.assertEqual(gamefield_pattern, [
            [0, 0, 0, 0, 0, 0],
            [0, 1, 1, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 0, 1, 1, 0],
            [0, 0, 0, 0, 0, 0]
        ])

    def test_c3_inject_pattern_smallersize(self):
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
        game.NR_ROWS = 5
        game.NR_COLS = 5
        gamefield_pre = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]
        gamefield_pattern = game.insert_pattern(gamefield_pre, beacon)
        self.assertEqual(gamefield_pattern, [
            [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ])

    def test_d1_create_from_file_biggersize(self):
        """
        Test creating gamefield from file with pattern.
        When gamefield is bigger than pattern
        """
        game.NR_ROWS = 10
        game.NR_COLS = 10
        gamefield = game.startvalues_fromfile("beacon")
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

    def test_d2_create_from_file_samesize(self):
        """
        Test creating gamefield from file with pattern.
        When gamefield is same size as pattern.
        """
        game.NR_ROWS = 6 # len of beacon
        game.NR_COLS = 6 # len of beacon[0]
        gamefield = game.startvalues_fromfile("beacon")
        self.assertEqual(gamefield, [
            [0, 0, 0, 0, 0, 0],
            [0, 1, 1, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 0, 1, 1, 0],
            [0, 0, 0, 0, 0, 0]
        ])

    def test_d3_create_from_file_smallersize(self):
        """
        Test creating gamefield from file with pattern.
        When gamefield is smaller
        """
        game.NR_ROWS = 5 # len of beacon is 6
        game.NR_COLS = 5 # len of beacon[0] is 6
        gamefield = game.startvalues_fromfile("beacon")
        self.assertEqual(gamefield, [
            [0, 0, 0, 0, 0, 0],
            [0, 1, 1, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 0, 1, 1, 0],
            [0, 0, 0, 0, 0, 0]
        ])

    def test_d4_create_from_file_smalldiffsize(self):
        """
        Test creating gamefield from file with pattern.
        When gamefield is smaller and pattern size diff between
        rows and cols
        """
        game.NR_ROWS = 5 # len of beacon is 6
        game.NR_COLS = 5 # len of beacon[0] is 6
        with self.assertRaises(ValueError):
            gamefield = game.startvalues_fromfile("beehive")

    def test_d5_create_from_file_no_file(self):
        """
        Test creating gamefield from file with pattern.
        When no such file
        """
        with self.assertRaises(FileNotFoundError):
            gamefield = game.startvalues_fromfile("no_such_file")


if __name__ == '__main__':
    unittest.main(verbosity=2)
