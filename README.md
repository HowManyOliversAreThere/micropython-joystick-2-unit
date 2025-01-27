# MicroPython Joystick 2 Unit

This repository houses a [MicroPython](https://micropython.org) driver for the M5Stack [Joystick 2 Unit](https://docs.m5stack.com/en/unit/Unit-JoyStick2).

It allows you to:

- Read the current X and Y values of the joystick
- Read whether the button is pressed or not

Features not yet implemented:

- Controlling the inbuilt RGB LED
- Reading the value of the inbuilt RGB LED
- Triggering an interrupt when the button is pressed
- `mip` installability

## Examples

Below is a minimal example of setting up the peripheral and then reading values from it. See the `examples` folder for example code demonstrating all of the capabilities of the device.

```python
from machine import I2C, Pin
import unit_joystick2

i2c = I2C(scl=Pin(32), sda=Pin(26))  # Pins for the ATOM Lite Grove port
joystick = unit_joystick2.UnitJoystick2(i2c)
print(f"x: {joystick.get_x()}, y: {joystick.get_y()}, button: {joystick.is_pressed()}")
```
