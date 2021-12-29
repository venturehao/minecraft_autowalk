import time
from random import randrange
import mouse
from pynput.keyboard import Key, Controller

keyboard = Controller()
start_wait = 15


direction = 1

def rand_walk():
    global direction
    
    while True:
        print("Walk")
        keyboard.press("w")
        time.sleep(randrange(5,10))
        keyboard.release("w")
        
        
        direction = 0.6*direction + 0.4* (1-randrange(2)*2)
        strength = randrange(3,20)
        print("Turn direction: %f with strenth %d" % (direction, strength))
        for i in range(strength):
            time.sleep(0.2)
            mouse._os_mouse.move_relative(direction*50, 0)
print("Wait {0} seconds to start auto walk, prepare your game ...".format(start_wait))
time.sleep(15)
rand_walk()

