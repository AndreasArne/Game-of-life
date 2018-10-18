#!/usr/bin/python3
"""
Functions for creating the gamefield used in Game of life
"""

from sys import argv
from random import randint

import json
import config

def inject_pattern(gamefield, pattern):
    """
    Inject pattern into center of the gamefield
    """
    rstart = (config.NR_ROWS // 2) - (len(pattern) // 2)
    rstop = rstart + len(pattern)

    cstart = (config.NR_COLS // 2) - (len(pattern[0]) // 2)
    cstop = cstart + len(pattern[0])

    count = 0
    for row in range(rstart, rstop):
        gamefield[row][cstart:cstop] = pattern[count]
        count += 1
    return gamefield

def get_pattern(filename):
    """
    Create 2d gamefield from file
    """
    file_path = "{}/{}.json".format(config.PATTERN_PATH, filename)
    with open(file_path, "r") as fh:
        pattern = json.load(fh)
    return pattern

def startvalues_fromfile(filename):
    """
    Create 2d gamefield from file
    """
    pattern = get_pattern(filename)
    if len(pattern) >= config.NR_ROWS  and len(pattern) == len(pattern[0]):
        config.NR_ROWS = len(pattern)
        config.NR_COLS = len(pattern[0])
        return pattern
    elif len(pattern) != len(pattern[0]) and (len(pattern) > config.NR_ROWS or len(pattern[0]) > config.NR_COLS):
        raise ValueError("Pattern does not have same size and is bigger than gamefield")
    else:
        return inject_pattern(create_2dlist(), pattern)

def create_2dlist():
    """
    create 2d list used for gamefield
    """
    return [[0 for i in range(config.NR_COLS)] for j in range(config.NR_ROWS)]

def random_startvalues():
    """
    Randomize start values on the gamefield
    """
    assert config.NR_ROWS == config.NR_COLS, "Number of rows and columns need to be the same!"

    gamefield = create_2dlist()
    for row in range(config.NR_ROWS):
        for col in range(config.NR_COLS):
            if randint(1, 10) > 6:# Arbitrary check if value should be 1 or not
                gamefield[row][col] = 1
    return gamefield

def check_if_cmdinp():
    """
    Check if there is a commandline argument for reading patterns from file
    """
    if len(argv) > 1:
        return argv[1]
    else:
        return ""

def create_gamefield():
    """
    Return a 2d array as gamefiled
    """
    filename = check_if_cmdinp()
    if filename:
        gamefield = startvalues_fromfile(filename)
    else:
        gamefield = random_startvalues()
    return gamefield
