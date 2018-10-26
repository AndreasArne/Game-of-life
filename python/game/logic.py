#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Implementation of Conway's game of life
"""
from time import sleep

from game import create_gamefield as cg
from game import turtle_gui as gui
from game import config



def start():    # pragma: no cover
    """
    Entry point for game.
    """
    gamefield = cg.create_gamefield()

    gui.init_screen()
    gui.config(config.NR_ROWS, config.NR_COLS)
    gui.create_turtles(config.NR_ROWS, config.NR_COLS)
    
    gui.update_board(gamefield)

    game_loop(gamefield)

def game_loop(gamefield):   # pragma: no cover
    """
    Forever loop for game
    """
    while(True):
        # prettyprint(gamefield)
        sleep(config.SLEEP_TIME)
        perform_tick(gamefield)
        gui.update_board(gamefield)

def get_tick_changes(gamefield):
    """
    Calculate changes on gamefield for tick
    """
    tick_changes = []
    for row in range(config.NR_ROWS):
        for col in range(config.NR_COLS):
            neighbor_value = get_neighborhood(gamefield, row, col)
            rule = check_rules(gamefield[row][col], neighbor_value)
            if rule > 0:
                tick_changes.append((row, col, rule))
    return tick_changes

def perform_tick(gamefield):
    """
    Perfom a tick.
    A tick is one round where each cell has a rule check
    """
    tick_changes = get_tick_changes(gamefield)
    activate_rules(gamefield, tick_changes)
    return gamefield

def check_rules(alive, n_value):
    """
    Check rules for cell
    """
    if not 0 <= n_value <= 8:
        raise ValueError("Impossible neighborhood value: ", n_value)

    elif alive and 0 <= n_value <= 1: # 1
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
            gamefield[row][col] = config.DEAD_V
        elif rule == 3:
            # Any live cell with more than three live neighbors dies, as if by overpopulation.
            gamefield[row][col] = config.DEAD_V
        elif rule == 4:
            # Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
            gamefield[row][col] = config.ALIVE_V
        else:
            # print("This shouldn't be!")
            # print(alive, n_value)
            raise ValueError("This shouldn't happen!" + str(change))
            pass
    return gamefield

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
    return index == config.NR_COLS-1

def calc_bounds(index, type_of):
    """
    calculate value if out of bounds with modulus
    """
    return index % config.NR_ROWS if type_of == "r" else index % config.NR_COLS

def prettyprint(gamefield):
    """
    Make a pretty print of the gamefield.
    """
    print(chr(27) + "[2J" + chr(27) + "[;H")
    print('\n'.join([' '.join([str(col) for col in row]) for row in gamefield]))

if __name__ == "__main__":
    start()
