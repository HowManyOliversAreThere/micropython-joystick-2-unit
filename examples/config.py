from machine import I2C, Pin

import unit_joystick2

SCL = 32
SDA = 26

i2c = I2C(scl=Pin(SCL), sda=Pin(SDA))
joystick = unit_joystick2.UnitJoystick2(i2c)
