from turtle import *
import random
objpxy = 1
delay(0)
ht()
def dot():
   pendown()
   forward(1)
   backward(2)
   forward(1)
   left(90)
   forward(1)
   backward(2)
   forward(1)
   right(90)
   penup()
speed(0)
penup()
setpos(-600, -600)
angle1 =pos()
a1x,a1y=angle1
dot()
setpos(-600, 600)
angle2 =pos()
a2x,a2y=angle2
dot()
setpos(600, -600)
angle3 =pos()
a3x,a3y=angle3
dot()
setpos(600, 600)
angle4 = pos()
a4x, a4y=angle4
dot()
midxy = (a1x+a2x)/2, (a1y+a2y)/2
midpx, midpy=midxy
setpos(midpx, midpy)
forward(110)
dot()
while(True):
    objp=random.randrange(1, 5)
    exec("objpxy = angle" + str(objp))
    objpx, objpy=objpxy
    cposx, cposy = pos()
    desx = (objpx+cposx)/3
    desy = (objpy+cposy)/3
    setpos(desx, desy)
    dot()