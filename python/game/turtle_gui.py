#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Code for the GUI used by game.py
"""
from turtle import Turtle, Screen



SCREEN = None
TURTLES = []
T_CONF = {
    "show_color": "white",
    "hide_color": "grey",
    "shape": "square",
    "size": 20,
    "border_size": 5
}



def init_screen(): # pragma: no cover
    """
    Initialize SCREEN with a screen()
    """
    global SCREEN
    SCREEN = Screen()



def config(nr_rows, nr_cols, bgcolor="black"):
    """
    Configure window
    """
    height = T_CONF["size"] * nr_rows + (T_CONF["border_size"] * nr_rows)
    width = T_CONF["size"] * nr_cols + (T_CONF["border_size"] * nr_cols)


    SCREEN.clear()
    SCREEN.setup(width, height)
    SCREEN.setworldcoordinates(-T_CONF["size"], width, height, -T_CONF["size"])
    SCREEN.colormode(255)
    SCREEN.bgcolor(bgcolor)
    SCREEN.tracer(0, 0) # turn of animations and delay
    SCREEN.title("Game of life")



def config_turtle(t):
    """
    Configure a Turtle
    """
    t.speed("fastest")
    t.shape(T_CONF["shape"])
    t.color(T_CONF["hide_color"])
    t.resizemode("user")
    t.shapesize(0.95, 0.95)



def place_turtle(t, x, y):
    """
    Place Turtle on x,y coordinate
    """
    if x >= SCREEN.window_width() or y >= SCREEN.window_height():
        raise IndexError("Placing Turtl outside of screen: x={}, y={}".format(x, y))
    t.up()
    t.goto(x, y)
    t.down()



def create_turtle(x, y):
    """
    Create and place a turtle
    """
    t = Turtle()
    config_turtle(t)
    x_pos = (x * T_CONF["size"]) + (x * T_CONF["border_size"])
    y_pos = (y * T_CONF["size"]) + (y * T_CONF["border_size"])
    place_turtle(t, x_pos, y_pos)
    return t



def create_turtles(rows, cols):
    """
    Create a turtle for each "pixel" in grid gui
    """
    if rows < 0 or cols < 0:
        raise IndexError("Siez less than 0")

    for x in range(rows):
        row = []
        for y in range(cols):
            row.append(create_turtle(x, y))
        TURTLES.append(row)



def hide_all_turtles():
    """
    hide all turtles on gamefield
    """
    for row in TURTLES:
        for t in row:
            t.hideturtle()



def update_turtle(x, y, new_value):
    """
    Change Turtle color
    """
    if new_value:
        # TURTLES[x][y].showturtle()
        TURTLES[x][y].color(T_CONF["show_color"])
    else:
        # TURTLES[x][y].hideturtle()
        TURTLES[x][y].color(T_CONF["hide_color"])



def update_board(gamefield):
    """
    Update colors for the Turtles based on value in gamefield
    """
    for x, row in enumerate(gamefield):
        for y, value in enumerate(row):
            update_turtle(x, y, value)
    SCREEN.update()



if __name__ == "__main__":
    pass
