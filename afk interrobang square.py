#Imports
from pynput.mouse import Controller
import random

#Initial setup and variables to start with so mouse isn't totally fucked
mouse = Controller()
mposX, mposY = mouse.position

#Ask user how much the shit should move, really funny when they say like 100 or smth
amount = int(input("How much movement? (px, use whole number):"))

#funnee loop
while True:

    #getting the mouse position as variables every iteration so that it actually, yk, moves
    mposX, mposY = mouse.position

    #Getting the places to move the mouse - each cooridnate moves a random amount between the negative amount that we asked for plus the current position to the amount plus move position
    mposmoveX = mposX
    mposmoveY = (0-amount) + mposY

    #Actually moves the mouse
    mouse.position = (mposmoveX, mposmoveY)
    mposX, mposY = mouse.position
    #Getting the places to move the mouse - each cooridnate moves a random amount between the negative amount that we asked for plus the current position to the amount plus move position
    mposmoveX = amount + mposX
    mposmoveY = mposY

    #Actually moves the mouse
    mouse.position = (mposmoveX, mposmoveY)
    mposX, mposY = mouse.position
    #Getting the places to move the mouse - each cooridnate moves a random amount between the negative amount that we asked for plus the current position to the amount plus move position
    mposmoveX = mposX
    mposmoveY = (amount) + mposY

    #Actually moves the mouse
    mouse.position = (mposmoveX, mposmoveY)
    mposX, mposY = mouse.position
    #Getting the places to move the mouse - each cooridnate moves a random amount between the negative amount that we asked for plus the current position to the amount plus move position
    mposmoveX = (0 - amount) + mposX
    mposmoveY =  mposY

    #Actually moves the mouse
    mposX, mposY = mouse.position
#BE CAREFUL - there is no failsafe on this so use a text editor or compiler that has a command built in
