#!/usr/bin/env python3

import random
import time

from tektronix import tek_mode, vt100_mode, clear, line, move_to, line_to, US


if __name__ == "__main__":
    tek_mode()
    clear()
    move_to(0, 700)
    print(US + "Fun with Tektronix")

    # 200 lines
    for _ in range(200):
        line(
            random.randint(0, 1023),
            random.randint(0, 767),
            random.randint(0, 1023),
            random.randint(0, 767),
        )
        print()
        time.sleep(0.05)
    time.sleep(5)

    clear()

    # 200 4-vertex polylines
    for _ in range(200):
        move_to(random.randint(0, 1023), random.randint(0, 767))
        line_to(random.randint(0, 1023), random.randint(0, 767))
        line_to(random.randint(0, 1023), random.randint(0, 767))
        print()
        time.sleep(0.05)
    time.sleep(5)

    vt100_mode()
