#!/usr/bin/python3
"""
Run test suites for game of life
"""
import unittest
# import your test modules
import test_create_gamefield
import test_game

# initialize the test suite
loader = unittest.TestLoader()
suite = unittest.TestSuite()

# add tests to the test suite
suite.addTests(loader.loadTestsFromModule(test_create_gamefield))
suite.addTests(loader.loadTestsFromModule(test_game))

# initialize a runner, pass it your suite and run it
runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)