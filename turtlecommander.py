import turtle
import pynput
from pynput.keyboard import Key, Listener
from turtle import *


def on_press(key):
    k = str(key).replace("'", "")
    turtle.speed(0)
    if (k == 'd'):
        turtle.setheading(0)
        turtle.forward(10)
    elif (k == 'w'):
        turtle.setheading(90)
        turtle.forward(10)
    elif (k == 'a'):
        turtle.setheading(180)
        turtle.forward(10)
    elif (k == 's'):
        turtle.setheading(270)
        turtle.forward(10)
    elif (k == "x"):
        turtle.setheading(90)
        turtle.forward(10)
        turtle.setheading(0)
        turtle.forward(10)
        turtle.setheading(270)
        turtle.forward(10)
        turtle.setheading(180)
        turtle.forward(10)
    elif (k == 'l'):
        turtle.pu()
    elif (k == 'k'):
        turtle.pd()
    elif (k == 'i'):
        turtle.color(0, 0, 0)
    elif (k == 'o'):
        turtle.color('white')
    elif (k == 'Key.left'):
        turtle.left(5)
    elif (k == 'Key.right'):
        turtle.right(5)
    elif (k == 'Key.up'):
        turtle.forward(10)
    elif (k == 'Key.down'):
        turtle.forward(10)
    print(key)

with Listener(on_press=on_press) as listener:
    listener.join()
