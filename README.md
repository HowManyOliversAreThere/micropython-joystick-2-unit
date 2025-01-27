# MicroPython Joystick 2 Unit

This repository houses a [MicroPython](https://micropython.org) driver for the M5Stack [Joystick 2 Unit](https://docs.m5stack.com/en/unit/Unit-JoyStick2).

It allows you to:

- Read the current X and Y values of the joystick
    - Either integer (0 - 65535) or float (0.0 - 1.0)
- Read whether the button is pressed or not
- Control the inbuilt RGB LED
- Read the value of the inbuilt RGB LED
- Read the Bootloader and Firmware version of the device

## Usage

Below is a minimal example of setting up the peripheral and then reading values from it.

```python
from machine import I2C, Pin
import joystick_2_unit

i2c = I2C(scl=Pin(32), sda=Pin(26))  # Pins for the ATOM Lite Grove port
joystick = joystick_2_unit.Joystick2Unit(i2c)
joystick.set_led(253, 176, 192)
print(
    f"x: {joystick.get_x()}, y: {joystick.get_y()},"
    f" button: {joystick.is_pressed()}, led: {joystick.get_led()}"
)
```

See the `examples` folder for example code demonstrating all of the capabilities of the device. To run these, first modify `examples/config.py` to match the pins used for your board, and then you can use `mpremote` to mount and run the code. Eg:

```bash
mpremote mount .
from examples import print_status
```

## Installation

The easiest way to install the package is using [mip](https://docs.micropython.org/en/latest/reference/packages.html#installing-packages-with-mip) via [mpremote](https://docs.micropython.org/en/latest/reference/mpremote.html):

```bash
mpremote mip install github:HowManyOliversAreThere/micropython-joystick-2-unit
```

Alternatively just grab `joystick_2_unit.py` and load it however you like.
