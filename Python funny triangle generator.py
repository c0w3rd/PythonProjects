from turtle import *
import random
objpxy = 1
delay(0)
ht()
def dot():
    pendown()
    forward(0.5)
    backward(1)
    forward(0.5)
    left(90)
    forward(0.5)
    backward(1)
    forward(0.5)
    right(90)
    penup()
speed(0)
penup()
setpos(-400, -400)
angle1 = pos()
a1x, a1y = angle1
dot()
setpos(0, 400)
angle2 = pos()
a2x, a2y = angle2
dot()
setpos(400, -400)
angle3 = pos()
a3x, a3y = angle3
dot()
midxy = (a1x+a2x)/2, (a1y+a2y)/2
midpx, midpy=midxy
setpos(midpx, midpy)
forward(110)
dot()
while(True):
    objp = random.randint(1, 3)
    exec("objpxy = angle" + str(objp))
    objpx, objpy=objpxy
    cposx, cposy = pos()
    desx = (objpx+cposx)/2
    desy = (objpy+cposy)/2
    setpos(desx, desy)
    dot()