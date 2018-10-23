#!/usr/bin/python3
"""
Run test suites for game of life
"""
import unittest
from sys import exit
# import your test modules
import test_create_gamefield
import test_game
import test_gui

# initialize the test suite
loader = unittest.TestLoader()
suite = unittest.TestSuite()

# add tests to the test suite
suite.addTests(loader.loadTestsFromModule(test_create_gamefield))
suite.addTests(loader.loadTestsFromModule(test_game))
suite.addTests(loader.loadTestsFromModule(test_gui))

# initialize a runner, pass it your suite and run it
runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)

# exit with status
exit(not result.wasSuccessful())
