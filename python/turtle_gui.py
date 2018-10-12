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
        "border_size": 4
    }

def config_turtle(t):
    t.shape(T_CONF["shape"])
    t.color(T_CONF["hide_color"])



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



def config( nr_rows, nr_cols, width=500, height=500, bgcolor="black"):
    SCREEN.reset()
    SCREEN.setup(width, height)
    SCREEN.setworldcoordinates(0, width, height, 0)
    SCREEN.colormode(255)
    SCREEN.bgcolor(bgcolor)

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



def start():
    """
    Deprecated. Functions only needed if using interactive window.
    """
    pass
    # SCREEN.exitonclick()
    # SCREEN.mainloop()



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



def main():
    """
    This wont work. Start using game.py
    """
    config()
    turtles = create_turtles(5)

    create_squares(turtles)
    update_board([])
    start()

if __name__ == "__main__":
    main()