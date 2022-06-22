from djitellopy import tello
from time import sleep

me = tello.Tello()
me.connect()

print(me.get_battery())

me.takeoff()
me.move_forward(50)
me.move_back(50)
me.land()

print(me.get_battery())