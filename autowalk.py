import time, platform, pynput
from random import randrange

kc = pynput.keyboard.Controller()
mc = pynput.mouse.Controller()
start_wait = 15

move_relative = None
if "Darwin" in platform.system():
    import Quartz
    def osx_move_relative(dx, dy, delay=0.2):
        ev = Quartz.CGEventCreateMouseEvent(None, Quartz.kCGEventMouseMoved, mc.position, Quartz.kCGMouseButtonLeft)
        Quartz.CGEventSetIntegerValueField(ev, Quartz.kCGMouseEventDeltaX, dx)
        Quartz.CGEventSetIntegerValueField(ev, Quartz.kCGMouseEventDeltaY, dy)
        Quartz.CGEventPost(Quartz.kCGHIDEventTap, ev)
        time.sleep(delay)
    move_relative = osx_move_relative
else:
    import mouse
    def win_move_relative(dx, dy, delay=0.2):
        mouse._os_mouse.move_relative(dx, dy)
        time.sleep(delay)
    move_relative = win_move_relative

direction = 1

def rand_walk():
    global direction
    
    while True:
        print("Walk")
        kc.press("w")
        time.sleep(randrange(5,10))
        kc.release("w")
        
        
        direction = 0.6*direction + 0.4* (1-randrange(2)*2)
        strength = randrange(3,20)
        print("Turn direction: %f with strenth %d" % (direction, strength))
        for i in range(strength):
            move_relative(direction*50, 0)
print("Wait {0} seconds to start auto walk, prepare your game ...".format(start_wait))
time.sleep(start_wait)
rand_walk()

