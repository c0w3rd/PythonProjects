import pynput
from pynput.mouse import Controller, Button
import random
mouse = Controller()
mposX, mposY = mouse.position
amount = int(input("How much movement? (px, use whole number):"))
while True:
    mposX, mposY = mouse.position
    mposmoveX = random.uniform((0.0 - float(mposX+amount)), (mposX+amount))
    mposmoveY = random.uniform((0.0 - float(mposY+amount)), (mposY+amount))
    mouse.position = (mposmoveX, mposmoveY)