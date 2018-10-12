from turtle import Turtle, Screen
from random import randint

SCREEN = Screen()
T_CONF = {
        "color": "white",
        "shape": "hide"
    }

def start():
    SCREEN.exitonclick()
    SCREEN.mainloop()



def config():
    SCREEN.reset()
    SCREEN.setup(500, 500)
    SCREEN.setworldcoordinates(0, 500, 500, 0)
    SCREEN.colormode(255)
    SCREEN.bgcolor("black")



def config_turtle(t):
    if T_CONF["shape"] == "hide":
        t.hideturtle()
    else:
        t.shape(T_CONF["shape"])        

    t.color(T_CONF["color"])



def draw_square(t, x, y, length):
    t.up()
    t.goto(x,y)
    t.down()
    t.begin_fill()
    for steps in range(4):

        t.fd(length)
        t.left(90)

    t.end_fill()



def create_squares(turtles):
    
    for i, t in enumerate(turtles):
        # x, y = randint(0, 200), randint(0, 200)
        draw_square(t, i*10, i*10, 10)



def create_turtles(number):
    turtles = []
    for i in range(number):
        t = Turtle()
        config_turtle(t)
        turtles.append(t)
    return turtles



def main():
    config()
    turtles = create_turtles(5)
    
    create_squares(turtles)
    
    start()



main()