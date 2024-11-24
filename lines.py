#!/usr/bin/env python3

import random
import time

from tektronix import tek_mode, vt100_mode, clear, line


if __name__ == "__main__":
    tek_mode(True)
    clear()
    for _ in range(200):
        line(
            random.randint(0, 1023),
            random.randint(0, 767),
            random.randint(0, 1023),
            random.randint(0, 767),
        )
        print("Tek")
        time.sleep(0.05)
    time.sleep(5)
    tek_mode(False)
    vt100_mode()
