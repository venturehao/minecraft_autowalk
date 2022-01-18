import time, platform, pynput
from random import randrange

kc = pynput.keyboard.Controller()
mc = pynput.mouse.Controller()
start_wait = 15

move_relative = None
left_down = None
left_up = None
right_down = None
right_up = None
if "Darwin" in platform.system():
    import Quartz
    def osx_move_relative(dx, dy, delay=0.2):
        ev = Quartz.CGEventCreateMouseEvent(None, Quartz.kCGEventMouseMoved, mc.position, Quartz.kCGMouseButtonLeft)
        Quartz.CGEventSetIntegerValueField(ev, Quartz.kCGMouseEventDeltaX, dx)
        Quartz.CGEventSetIntegerValueField(ev, Quartz.kCGMouseEventDeltaY, dy)
        Quartz.CGEventPost(Quartz.kCGHIDEventTap, ev)
        time.sleep(delay)

    def osx_mouse_click_left_down():
        ev = Quartz.CGEventCreateMouseEvent(None, Quartz.kCGEventLeftMouseDown, mc.position, Quartz.kCGMouseButtonLeft)
        Quartz.CGEventPost(Quartz.kCGHIDEventTap, ev)

    def osx_mouse_click_left_up():
        ev = Quartz.CGEventCreateMouseEvent(None, Quartz.kCGEventLeftMouseUp, mc.position, Quartz.kCGMouseButtonLeft)
        Quartz.CGEventPost(Quartz.kCGHIDEventTap, ev)

    def osx_mouse_click_right_down():
        ev = Quartz.CGEventCreateMouseEvent(None, Quartz.kCGEventRightMouseDown, mc.position, Quartz.kCGMouseButtonRight)
        Quartz.CGEventPost(Quartz.kCGHIDEventTap, ev)

    def osx_mouse_click_right_up():
        ev = Quartz.CGEventCreateMouseEvent(None, Quartz.kCGEventRightMouseUp, mc.position, Quartz.kCGMouseButtonRight)
        Quartz.CGEventPost(Quartz.kCGHIDEventTap, ev)



    move_relative = osx_move_relative
    left_down = osx_mouse_click_left_down
    left_up = osx_mouse_click_left_up
    right_down = osx_mouse_click_right_down
    right_up = osx_mouse_click_right_up
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
        print("Walk forward")
        kc.press("w")
        time.sleep(randrange(5,10))
        kc.release("w")

        left_down()
        time.sleep(randrange(4,6))
        left_up()
        
        kc.press("w")
        time.sleep(randrange(2,4))
        kc.release("w")

        right_down()
        time.sleep(randrange(2,4) * 0.1)
        right_up()

        x = str(randrange(3))
        kc.press(x)
        time.sleep(randrange(2,4) * 0.1)
        kc.release(x)

        mp = {0:"a", 1:"s", 2:"d"}

        x = mp[randrange(3)]
        print("walk", x)
        kc.press(x)
        time.sleep(randrange(3,5))
        kc.release(x)
        
        direction = 0.6*direction + 0.4* (1-randrange(2)*2)
        strength = randrange(3,20)


        ts = randrange( 30,50)
        print("Sleep for: %d seconds" % ts)
        time.sleep(ts)

        print("Turn direction: %f with strenth %d" % (direction, strength))
        for i in range(strength):
            move_relative(direction*50, 0)
print("Wait {0} seconds to start auto walk, prepare your game ...".format(start_wait))
time.sleep(start_wait)
rand_walk()
