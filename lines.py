#!/usr/bin/env python3

import random

from tektronix import tek_mode, vt100_mode, clear, line


if __name__ == '__main__':
    tek_mode()
    clear()
    for _ in range(200):
        line(
            random.randint(0, 1023), random.randint(0, 767),
            random.randint(0, 1023), random.randint(0, 767))
    vt100_mode()
