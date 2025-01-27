# A MicroPython driver for the Unit Joystick2
# https://docs.m5stack.com/en/unit/Unit-JoyStick2

from machine import I2C


class Joystick2Unit:
    i2c: I2C
    addr: int

    def __init__(self, i2c, addr=0x63):
        self.i2c = i2c
        self.addr = addr
        assert self.check_address(), (
            "Unit Joystick2 not found at I2C address 0x%02x" % addr
        )

    def check_address(self) -> bool:
        """Read address register, return True if the address is correct"""
        result = self.i2c.readfrom_mem(self.addr, 0xFF, 1)
        return result == bytes([self.addr])

    def _read_2_byte_int(self, reg) -> int:
        """Read a 2-byte signed integer from the specified register"""
        result = self.i2c.readfrom_mem(self.addr, reg, 2)
        return int.from_bytes(result, "little")

    def get_x(self) -> float:
        """Return the x-axis position as a float from 0-1"""
        return self._read_2_byte_int(0x00) / 65535.0

    def get_y(self) -> float:
        """Return the y-axis position as a float from 0-1"""
        return self._read_2_byte_int(0x02) / 65535.0

    def is_pressed(self) -> bool:
        """Return True if the button is pressed"""
        return self.i2c.readfrom_mem(self.addr, 0x20, 1) != b"\x01"
