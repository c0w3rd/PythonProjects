from pynput.mouse import Controller
import random
mouse = Controller()
mposX, mposY = mouse.position
amount = int(input("How much movement? (px, use whole number):"))

while True:
    mposX, mposY = mouse.position
    mposmoveX = random.randint((0 - amount) + mposX, amount + mposX)
    mposmoveY = random.randint((0 - amount) + mposY, amount + mposY)
    mouse.position = (mposmoveX, mposmoveY)
