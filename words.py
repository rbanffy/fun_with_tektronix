#!/usr/bin/env python3

import random
import time

from tektronix import tek_mode, vt100_mode, clear, move_to, text_size


if __name__ == "__main__":
    tek_mode(True)
    clear()
    for _ in range(10):
        text_size(random.randint(0, 7))
        move_to(random.randint(0, 1023), random.randint(0, 767))
        print("Tektronix")
        time.sleep(0.05)
    time.sleep(5)
    vt100_mode()
    # tek_mode(False)
