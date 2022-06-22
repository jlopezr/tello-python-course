import keypress as kp
from djitellopy import tello
from time import sleep

def getKeyboard():
    lr, fb, ud, yv = 0,0,0,0
    speed = 50

    if kp.getKey("LEFT"): lr = -speed
    elif kp.getKey("RIGHT"): lr = speed

    if kp.getKey("UP"): fb = speed
    elif kp.getKey("DOWN"): fb = -speed

    if kp.getKey("w"): ud = speed
    elif kp.getKey("s"): ud = -speed

    if kp.getKey("a"): yv = -speed
    elif kp.getKey("d"): yv = speed

    if kp.getKey("q"): me.land()
    if kp.getKey("e"): me.takeoff()

    return [lr, fb, ud, yv]

kp.init()
me = tello.Tello()
me.connect()
print(me.get_battery())

while True:
    values = getKeyboard()
    me.send_rc_control(values[0], values[1], values[2], values[3])