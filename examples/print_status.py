import time

from . import config

joystick = config.joystick

while True:
    x = joystick.get_x()
    y = joystick.get_y()
    is_pressed = joystick.is_pressed()

    print("x: %.02f, y: %.02f, pressed: %s" % (x, y, is_pressed))
    time.sleep(0.1)
