#A sorting algorithm I built because I thought it would be fun- took a surprisingly little amount of effort. Is it fast? Probably not. Do I know what kind it is? No. But it seems to work well enough.

setToUse = str(input("What set should the program use (preset/input): "))

presettobesorted = [1285, 9213, 4038, 2150, 3645, 5496, 5689, 6994, 6753, 3273, 7875, 5795, 6073, 9932, 4411, 2708, 8112, 7954, 6035, 2523, 5615, 8284, 2176, 1781, 5478, 3273, 8399, 2995, 1457, 5590, 9917, 5641, 7215, 3615, 9645, 3851, 8312, 5628, 9111, 7600, 587, 9078, 2388, 3185, 1870, 8835, 619, 7977, 9404, 5023, 9897, 9188, 8030, 5949, 3969, 8884, 1535, 591, 1762, 6472, 4028, 1315, 5314, 638, 3515, 7199, 1528, 1525, 2440, 1381, 3618, 8210, 2831, 2071, 6015, 3275, 6578, 1574, 1093, 93, 5821, 6152, 937, 4216, 6273, 463, 386, 9961, 3742, 2589, 1668, 9689, 5258, 5496, 5354, 8167, 4796, 114, 7551, 4283, 6744, 6631, 9622, 9908, 2341, 9836, 7369, 3898, 8521, 5376, 2034, 2600, 4997, 5575, 3209, 5068, 6522, 2970, 8797, 8165, 9103, 1931, 3902, 9675, 4342, 5411, 3169, 1749, 8087, 9110, 1630, 5598, 6958, 2597, 9248, 8579, 7382, 9332, 6861, 4567, 4381, 4786, 5876, 4451, 7818, 2644, 9467, 3513]
num1 = 0
num2 = 0
temp = 0

if setToUse == "preset":
    tobesorted = presettobesorted
elif setToUse == "input":
    numofnum = int(input("how mnay numers lmoaa: "))
    tobesorted = []
    for x in range(numofnum):
        inpnum = input("Numer " + str(x+1) + " yk? yea it go here: ")
        if inpnum == "":
            print("Entered nothing so using 0, moving on...")
            inpnum = int(0)
        tobesorted.append(int(inpnum))

direction = str(input("Low to high sort or high to low sort? (htl/lth): "))
print("Sorting...")

if direction == "lth":
    for x in range(len(tobesorted)):
        for x in range(len(tobesorted)-1):
            num1 = tobesorted[x]
            num2 = tobesorted [x+1]
            if num1 > num2:
                temp = num1
                num1 = num2
                num2 = temp
                tobesorted[x] = num1
                tobesorted[x+1] = num2

elif direction == "htl":
    for x in range(len(tobesorted)):
        for x in range(len(tobesorted)-1):
            num1 = tobesorted[x]
            num2 = tobesorted [x+1]
            if num2 > num1:
                temp = num1
                num1 = num2
                num2 = temp
                tobesorted[x] = num1
                tobesorted[x+1] = num2

print("| vv | Your sorted list below | vv |")
print(tobesorted)