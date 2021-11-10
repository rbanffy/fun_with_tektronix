#!/usr/bin/env python3

import random
import time

from tektronix import tek_mode, vt100_mode, clear, line


if __name__ == '__main__':
    print("\033]0;Fun with Tektronix\007")
    tek_mode()
    clear()
    for _ in range(200):
        line(
            random.randint(0, 1023), random.randint(0, 767),
            random.randint(0, 1023), random.randint(0, 767))
        time.sleep(.05)
    time.sleep(5)
    vt100_mode()
