#!/usr/bin/env python3

import random
import time

from tektronix import tek_mode, vt100_mode, clear, box, line_style


if __name__ == "__main__":
    tek_mode(True)
    clear()
    for _ in range(100):
        x1, y1 = random.randint(0, 1023), random.randint(0, 767)
        x2, y2 = random.randint(0, 1023), random.randint(0, 767)
        line_style(random.randint(0, 15))
        box(x1, y1, x2, y2)
        time.sleep(0.05)
    time.sleep(5)
    tek_mode(False)
    vt100_mode()
