import math
from time import sleep
import keypress as kp
import numpy as np
import cv2
from djitellopy import tello
import time

######## PARAMETERS ##########
fSpeed = 117/10 # forward speed in cm/s
aSpeed = 360/10 # angular speed degrees/s
interval = 0.25

dInterval = fSpeed * interval
aInterval = aSpeed * interval
#############################
x, y = 500, 500
yaw = 0

def getKeyboard():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50
    d = 0
    a = 0
    global x, y, yaw

    if kp.getKey("LEFT"):
        lr = -speed
        d = dInterval
        a = -180
    elif kp.getKey("RIGHT"):
        lr = speed
        d = -dInterval
        a = 180

    if kp.getKey("UP"):
        fb = speed
        d = dInterval
        a = 270
    elif kp.getKey("DOWN"):
        fb = -speed
        d = -dInterval
        a = -90

    if kp.getKey("w"):
        ud = speed
    elif kp.getKey("s"):
        ud = -speed

    if kp.getKey("a"):
        yv = -speed
        yaw = yaw + aInterval
    elif kp.getKey("d"):
        yv = speed
        yaw = yaw - aInterval

    if kp.getKey("q"): me.land(); time.sleep(3) #TODO Para que necesita estar parado 3 segundos?
    if kp.getKey("e"): me.takeoff()

    sleep(interval)
    a = a + yaw
    x += int(d * math.cos(math.radians(a)))
    y += int(d * math.sin(math.radians(a)))

    print((x,y,a))

    return [lr, fb, ud, yv, x, y]

def drawPoints(img, points):
    cv2.circle(img, (points[0], points[1]), 5, (0, 0, 255), cv2.FILLED)

kp.init()
me = tello.Tello()
me.connect()

print(me.get_battery())

img = np.zeros((1000, 1000, 3), np.uint8)

while True:
    values = getKeyboard()
    me.send_rc_control(values[0], values[1], values[2], values[3])

    points = (values[4], values[5])
    drawPoints(img,points)
    cv2.imshow("Output", img)
    cv2.waitKey(1)