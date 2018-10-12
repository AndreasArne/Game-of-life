#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Implementation of Conway's game of life
"""
from random import randint
from time import sleep
from sys import argv
import json

import turtle_gui as gui

NR_ROWS = 10
NR_COLS = 10
ALIVE_V = 1
DEAD_V  = 0
SLEEP_TIME = 0.5

def create_gamefield():
    """
    Return a 2d array as gamefiled
    """
    return init_game_from_file(argv[1]) if check_if_cmdinp() else init_game()

def start():
    """
    Entry point for game.
    """
    gamefield = create_gamefield()
    gui.config(NR_ROWS, NR_COLS)
    gui.start()
    gui.update_board(gamefield)

    game_loop(gamefield)

def game_loop(gamefield):
    """
    Forever loop for game
    """
    while(True):
        # prettyprint(gamefield)
        sleep(SLEEP_TIME)
        tick(gamefield)
        gui.update_board(gamefield)

def tick(gamefield):
    """
    Perfom a tick.
    A tick is one round where each cell has a rule check
    """
    tick_changes = []
    for row in range(NR_ROWS):
        for col in range(NR_COLS):
            neighbor_value = get_neighborhood(gamefield, row, col)
            rule = check_rules(gamefield[row][col], neighbor_value)
            if rule > 0:
                tick_changes.append((row, col, rule))

    activate_rules(gamefield, tick_changes)

def check_rules(alive, n_value):
    """
    Check rules for cell
    """
    if alive and n_value < 2: # 1
        # Any live cell with fewer than two live neighbors dies, as if by under population.
        return 1
    elif alive and 1 < n_value < 4: # 2-3
        # Any live cell with two or three live neighbors lives on to the next generation.
        return -1
    elif alive and n_value > 3: # > 3
        # Any live cell with more than three live neighbors dies, as if by overpopulation.
        return 3
    elif not alive and n_value == 3: # 3
        # Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
        return 4
    else:
        return -1

def activate_rules(gamefield, tick):
    """
    Activate rules for each changed cell
    """
    row_i    = 0
    col_i    = 1
    rule_i   = 2
    for change in tick:
        rule = change[rule_i]
        row = change[row_i]
        col = change[col_i]
        if rule == 1:
            # Any live cell with fewer than two live neighbors dies, as if by under population.
            gamefield[row][col] = DEAD_V
        elif rule == 3:
            # Any live cell with more than three live neighbors dies, as if by overpopulation.
            gamefield[row][col] = DEAD_V
        elif rule == 4:
            # Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
            gamefield[row][col] = ALIVE_V
        else:
            # print("This shouldn't be!")
            # print(alive, n_value)
            pass

def get_neighborhood(gamefield, r_index, c_index):
    """
    calculate neighborhood value for col to check rules
    """
    if check_bounds_column(c_index): # needed because of slicing
        above = sum(gamefield[calc_bounds(r_index-1, "r")][c_index-1:c_index+1], gamefield[calc_bounds(r_index-1, "r")][0])
        below = sum(gamefield[calc_bounds(r_index+1, "r")][c_index-1:c_index+1], gamefield[calc_bounds(r_index+1, "r")][0])
    else:
        above = sum([gamefield[calc_bounds(r_index-1, "r")][i] for i in range(c_index-1, c_index+2)])
        below = sum([gamefield[calc_bounds(r_index+1, "r")][i] for i in range(c_index-1, c_index+2)])

    left  = gamefield[r_index][calc_bounds(c_index-1, "c")]
    right = gamefield[r_index][calc_bounds(c_index+1, "c")]

    neighbor_sum = above + below + left + right
    return neighbor_sum

def check_bounds_column(index):
    """
    Check if range for col column index will be out-of-bounds.
    Only applicable for over size not below size, -1.
    """
    return index == NR_COLS-1

def calc_bounds(index, type_of):
    """
    calculate value if out of bounds with modulus
    """
    return index % NR_ROWS if type_of == "r" else index % NR_COLS

def init_game():
    """
    Create 2d gamefield
    """
    gamefield = [[0 for i in range(NR_COLS)] for j in range(NR_ROWS)]
    random_startvalues(gamefield)
    return gamefield

def random_startvalues(game):
    """
    Randomize start values on the gamefield
    """
    for row in range(NR_ROWS):
        for col in range(NR_COLS):
            if randint(1, 10) > 6:# Arbitrary check if value should be 1 or not
                game[row][col] = 1

def prettyprint(game):
    """
    Make a pretty print of the gamefield.
    """
    print(chr(27) + "[2J" + chr(27) + "[;H")
    print('\n'.join([' '.join([str(col) for col in row]) for row in game]))

def init_game_from_file(filename):
    """
    Create 2d gamefield from file
    """
    global NR_ROWS, NR_COLS
    file_path = "patterns/{}.json".format(filename)
    with open(file_path, "r") as fh:
        gamefield = json.load(fh)

    NR_ROWS = len(gamefield)
    NR_COLS = len(gamefield[0])
    return gamefield

def check_if_cmdinp():
    """
    Check if there is a commandline argument for reading patterns from file
    """
    if len(argv) > 1:
        return argv[1]
    else:
        return 0

if __name__ == "__main__":
    start()