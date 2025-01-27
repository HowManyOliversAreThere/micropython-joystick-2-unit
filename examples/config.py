from machine import SoftI2C, Pin

import joystick_2_unit

SCL = 32
SDA = 26

i2c = SoftI2C(scl=Pin(SCL), sda=Pin(SDA))
joystick = joystick_2_unit.Joystick2Unit(i2c)
