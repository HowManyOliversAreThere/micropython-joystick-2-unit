from micropython import const
import time

from . import config

joystick = config.joystick

print("Starting...")

# We use a movement threshold as the value of the joystick changes very slightly when
# it is not being moved. This is small enough to not impact the user experience, but
# minimises the number of LED updates we need to send.
MVMT_THRESHOLD = const(3)
# We use a threshold for the number of samples the button must be pressed for before
# we consider it to be pressed. This helps to reduce the button occasionally appearing
# to be pressed while moving it.
PRESS_THRESHOLD = const(5)

old_led = [0, 0, 0]  # Track previous LED values to avoid sending redundant updates
pressed_samples = 0

while True:
    x = joystick.get_x()
    y = joystick.get_y()
    if joystick.is_pressed():
        pressed_samples += 1
    elif pressed_samples > 0:
        pressed_samples = 0

    led = [int(x * 255), int(y * 255), 255 if pressed_samples >= PRESS_THRESHOLD else 0]
    delta = sum(abs(led[i] - old_led[i]) for i in range(3))
    if delta >= MVMT_THRESHOLD:
        print(f"Setting LED to [{led[0]:03d}, {led[1]:03d}, {led[2]:03d}]")
        joystick.set_led(*led)
        old_led = led

    time.sleep(0.01)
