import time

from . import config

joystick = config.joystick

joystick.set_led(50, 100, 150)
print(f"Bootloader version: {joystick.get_bootloader_version()}")
print(f"Firmware version: {joystick.get_firmware_version()}")
print(f"LED state: {joystick.get_led()}")

print("Starting...")
while True:
    x = joystick.get_x()
    y = joystick.get_y()
    is_pressed = joystick.is_pressed()

    print("x: %.02f, y: %.02f, pressed: %s" % (x, y, is_pressed))
    time.sleep(0.1)
