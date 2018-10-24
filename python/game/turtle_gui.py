#!/usr/bin/python3
# -*- coding: utf-8 -*-
from turtle import Turtle, Screen
from random import randint



SCREEN = Screen()
TURTLES = []
T_CONF = {
        "show_color": "white",
        "hide_color": "grey",
        "shape": "square",
        "size": 20,
        "border_size": 5
    }

def config_turtle(t):
    t.speed("fastest")
    t.shape(T_CONF["shape"])
    t.color(T_CONF["hide_color"])
    t.resizemode("user")
    t.shapesize(0.95, 0.95)



def place_turtle(t, x, y):
    t.up()
    t.goto(x,y)
    t.down()



def create_turtle(x, y):
    t = Turtle()
    config_turtle(t)
    x_pos = (x * T_CONF["size"]) + (x * T_CONF["border_size"])
    y_pos = (y * T_CONF["size"]) + (y * T_CONF["border_size"])
    place_turtle(t, x_pos, y_pos)
    return t



def create_turtles(rows, cols):
    global TURTLES
    for x in range(rows):
        row = []
        for y in range(cols):
            row.append(create_turtle(x, y))
        TURTLES.append(row)



def hide_all_turtles():
    for row in TURTLES:
        for t in row:
            t.hideturtle()



def config( nr_rows, nr_cols, bgcolor="black"):
    height = T_CONF["size"] * nr_rows + (T_CONF["border_size"] * nr_rows)
    width = T_CONF["size"] * nr_cols + (T_CONF["border_size"] * nr_cols)

    SCREEN.reset()
    SCREEN.setup(width, height)
    SCREEN.setworldcoordinates(-T_CONF["size"], width, height, -T_CONF["size"])
    SCREEN.colormode(255)
    SCREEN.bgcolor(bgcolor)
    SCREEN.tracer(0, 0) # turn of animations and delay
    SCREEN.title("Game of life")

    create_turtles(nr_rows, nr_cols)
    # hide_all_turtles()



def update_turtle(x, y, new_value):
    if TURTLES[x][y] != new_value:
        if new_value:
            # TURTLES[x][y].showturtle()
            TURTLES[x][y].color(T_CONF["show_color"])
        else:
            # TURTLES[x][y].hideturtle()
            TURTLES[x][y].color(T_CONF["hide_color"])



def update_board(gamefield):
    for x, row in enumerate(gamefield):
        for y, value in enumerate(row):
            update_turtle(x, y, value)
    SCREEN.update()



def draw_square(t, x, y, length):
    """
    deprecated
    """
    t.up()
    t.goto(x,y)
    t.down()
    t.begin_fill()
    for steps in range(4):
        t.fd(length)
        t.left(90)

    t.end_fill()



def create_squares(turtles):
    """
    deprecated
    """
    size = T_CONF["size"]

    for x, row in enumerate(turtles):
        for y, t in enumerate(row):
            draw_square(t, x*size, y*size, size)



if __name__ == "__main__":
    pass