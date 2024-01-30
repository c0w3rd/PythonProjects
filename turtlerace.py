import turtle
import random
import time

master = turtle.Turtle()
turtle.Screen().bgcolor("gray")
master.pu()
master.speed(0)
master.goto(-2000, 350)
master.pd()
master.fd(6000)
master.pu()
master.goto(-2000, 25)
master.pd()
master.fd(6000)
master.pu()
master.goto(-2000, -300)
master.pd()
master.fd(6000)

try:
    numT = int(input("How many turtles do you want to race? "))
except:
    print("Use a number in numeric form")
    exit()

turtles = []
turtles2 = []
tIds = []
letters = ['a', 'b', 'c', 'd', 'e', 'f']
colors = ["red", "orange", "green", "blue", "purple"]

turtleInitDelta = 0
tSpacing = 20
tWon = 0
tIndex = 0


try:
    for x in range(numT):
        turtles.append("turtle" + str(x))

    for t in turtles:
        #setuppp :3
        t = turtle.Turtle()
        turtles2.append(t)
        t.speed(0)
        t.pu()
        t.fd(0-((tSpacing*len(turtles))/2))
        t.fd(turtleInitDelta)
        turtleInitDelta += tSpacing
        t.lt(90)
        t.fd(-300)
        t.speed(0)
        t.pd()
        t.color(colors[random.randint(0, 4)])
        tIndex += 1

        
    time.sleep(3)
    
    while(tWon == 0):
        for r in turtles2:
            r.fd((random.random()*10)+3)
            if r.ycor() >= 350:
                print(turtles[turtles2.index(r)] + " won the race!!")
                tWon = 1
    turtle.exitonclick()

except Exception as e:
    print("Something went wrong. Sorry!!")
    print(e)
    exit()