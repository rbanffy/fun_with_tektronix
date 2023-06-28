import sys

ESC = chr(27)

CR = chr(13)
CSI = ESC + "["
ETX = chr(3)
FF = chr(12)
FS = chr(28)
GS = chr(29)
US = chr(31)


def tek_mode():
    "Enter Tektronix mode"
    sys.stdout.write(CSI + "?38h" + CR)


def vt100_mode():
    "Goes back to VT100 mode"
    sys.stdout.write(ESC + ETX + CR)


def clear():
    "Clears the screen. On a real Tektronix, this flashes the screen"
    sys.stdout.write(ESC + FF + CR)


def coord(x: int, y: int):
    "Translates coordinates to Tek strings"
    if x < 0 or x > 1024 or y < 0 or y > 768:
        raise ValueError(f"Invalid coordinates ({x}, {y})")
    return (
        chr(32 + (y // 32))
        + chr(96 + (y & 31))
        + chr(32 + x // 32)
        + chr(64 + (x & 31))
    )


def line(x1: int, y1: int, x2: int, y2: int):
    """Draws a line from *x1, y1) to (x2, y2).

    Enters vector mode, draws the vector, then goes back to alpha mode
    leaving the cursor at the last coordinate.
    """
    sys.stdout.write(GS + CSI + coord(x1, y1) + coord(x2, y2) + US)


def move_to(x: int, y: int):
    """Moves the cursor to (x, y).

    Enters vector mode and moves the cursor to (x,y).
    """
    sys.stdout.write(GS + CSI + coord(x, y))


def line_to(x: int, y: int):
    """Draws a line from the current cursor position (in graph mode)
    to (x, y). Needs to be used in graph mode.

    When the last vector is drawn, you need to terminate graph mode.
    """
    sys.stdout.write(coord(x, y))
