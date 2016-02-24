import random

from tektronix import clear, line


if __name__ == '__main__':
    while True:
        clear()
        for _ in range(200):
            line(
                random.randint(0, 1023), random.randint(0, 767),
                random.randint(0, 1023), random.randint(0, 767))
