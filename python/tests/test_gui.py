#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Tests the functions used to for the gui in turtle_gui.py.
"""
from turtle import Turtle
from sys import path
import os
import unittest
path.insert(1, os.path.join(path[0], '..'))

from game import turtle_gui as gui
from game import config

class TestGui(unittest.TestCase):
    """
    Test the different functions used for in turtle_gui.py
    """

    @classmethod
    def setUpClass(cls):
        """
        Initalize scrren before running tests
        """
        gui.init_screen()

    def setUp(self):
        config.NR_COLS = 10
        config.NR_ROWS = 10
        gui.config(config.NR_ROWS, config.NR_COLS)

    def test_a1_config(self):
        """
        Test config() function for setting up a SCREEN
        """
        gui.config(config.NR_ROWS, config.NR_COLS, "red")

        self.assertEqual(gui.SCREEN.screensize(), (230, 230))
        # Don't know how to test new world coordinates
        self.assertEqual(gui.SCREEN.colormode(), 255)
        self.assertEqual(gui.SCREEN.bgcolor(), "red")
        self.assertEqual(gui.SCREEN.delay(), 0)
        self.assertEqual(gui.SCREEN.tracer(), 0)
        
    def test_b1_config_turtle(self):
        """
        Test config_turtle() function for setting up a Turtle
        """
        t = Turtle()
        gui.config_turtle(t)

        self.assertEqual(t.shape(), gui.T_CONF["shape"])
        self.assertEqual(t.speed(), 0)
        self.assertEqual(t.color(), (gui.T_CONF["hide_color"], gui.T_CONF["hide_color"]))
        self.assertEqual(t.resizemode(), "user")
        self.assertEqual(t.shapesize(), (0.95, 0.95, 1))

    def test_c1_place_turtle(self):
        """
        Test place_turtle() function for placing turtle on x,y coordinate
        """
        t = Turtle()
        gui.place_turtle(t, 0, 0)

        self.assertEqual(t.pos(), (0, 0))
        gui.place_turtle(t, 19, 18)
        self.assertEqual(t.pos(), (19, 18))

    def test_c2_place_turtle_outside(self):
        """
        Test place_turtle() function for placing turtle on x,y coordinate outside range of window size
        """
        t = Turtle()
        height = gui.SCREEN.window_height() + 20
        width = gui.SCREEN.window_width() + 20
        
        with self.assertRaises(IndexError):
            gui.place_turtle(t, width, height)

    def test_d1_create_turtle(self):
        """
        Test create_turtle() function for creating a Turtle and placing it.
        """
        t = gui.create_turtle(0, 0)
        ts = gui.SCREEN.turtles()
        self.assertEqual(t.pos(), (0, 0))
        self.assertIs(t, ts[0])

        t2 = gui.create_turtle(1, 1)
        ts = gui.SCREEN.turtles()
        self.assertEqual(t2.pos(), (25, 25))
        self.assertIs(t2, ts[1])

    def test_e1_create_turtles(self):
        """
        Test create_turtles() function for creating all Turtles and placing them.
        """
        gui.create_turtles(3, 3)
        self.assertEqual(gui.TURTLES[0][0].pos(), (0, 0))
        self.assertEqual(gui.TURTLES[2][2].pos(), (50, 50))
        self.assertIs(gui.TURTLES[0][0], gui.SCREEN.turtles()[0])

    def test_e2_create_turtles_negativ(self):
        """
        Test create_turtles() function for creating all Turtles and placing them.
        With negativ values
        """
        with self.assertRaises(IndexError):
            gui.create_turtles(-3, -3)

    def test_f1_hide_all_turtles(self):
        """
        Test hide_all_turtles() function.
        """
        gui.create_turtles(3, 3)
        gui.hide_all_turtles()
        for rows in gui.TURTLES:
            for t in rows:
                self.assertFalse(t.isvisible())

    def test_g1_update_turtle(self):
        """
        Test update_turtle() function.
        """
        gui.create_turtles(3, 3)
        gui.update_turtle(0, 0, 1)
        self.assertEqual(gui.TURTLES[0][0].color(), (gui.T_CONF["show_color"], gui.T_CONF["show_color"]))

        gui.update_turtle(1, 1, 0)
        self.assertEqual(gui.TURTLES[1][1].color(), (gui.T_CONF["hide_color"], gui.T_CONF["hide_color"]))

    def test_h1_update_board(self):
        """
        Test update_board() function.
        """
        gui.create_turtles(3, 3)
        gui.update_turtle(0, 0, 0)
        gamefield = [
            [0, 0, 1],
            [1, 0, 0],
            [0, 1, 0],
        ]
        gui.update_board(gamefield)
        self.assertEqual(gui.TURTLES[0][2].color(), (gui.T_CONF["show_color"], gui.T_CONF["show_color"]))
        self.assertEqual(gui.TURTLES[1][0].color(), (gui.T_CONF["show_color"], gui.T_CONF["show_color"]))
        self.assertEqual(gui.TURTLES[2][1].color(), (gui.T_CONF["show_color"], gui.T_CONF["show_color"]))
        self.assertEqual(gui.TURTLES[0][0].color(), (gui.T_CONF["hide_color"], gui.T_CONF["hide_color"]))

if __name__ == '__main__':
    unittest.main(verbosity=2)
