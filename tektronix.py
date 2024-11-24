import sys

GS = chr(29)  # Graph mode
US = chr(31)  # Alpha mode
ESC = chr(27)
FS = chr(28)  # Point plot mode
ETX = chr(3)
FF = chr(12)
CR = chr(13)  # Resets text column, finishes drawing
RS = chr(30)  # Incremental plot mode
CSI = ESC + "["


def tek_mode(tek_on: bool = False) -> None:
    "Enter/Leave Tektronix mode. Works on VT terminals"
    if tek_mode:
        sys.stdout.write(CSI + "?38h")
    else:
        sys.stdout.write(CSI + "?38l")


def vt100_mode() -> None:
    "Goes back to VT100 window. Works on xterm, not on VT terminals"
    sys.stdout.write(ESC + ETX)


def clear() -> None:
    "Clears the screen. On a real Tektronix, this flashes the screen white"
    sys.stdout.write(ESC + FF)


def coord(x: int, y: int) -> bytearray:
    """Translates coordinates to Tek strings.

    Converts two 10-bit unsigned integers into four 7-bit ascii symbols.
    """
    if x < 0 or x > 1024 or y < 0 or y > 768:
        raise ValueError("Invalid coordinates (%d, %d)" % (x, y))
    return (
        chr(32 + (y // 32))
        + chr(96 + (y & 31))
        + chr(32 + x // 32)
        + chr(64 + (x & 31))
    )


def text_size(n: int) -> None:
    sizes = ["8", "9", ":", ";", "0", "1", "2", "3"]
    sys.stdout.write(ESC + sizes[n] + CR)


def move_to(x: int, y: int) -> None:
    sys.stdout.write(GS + coord(x, y))


def line(x1: int, y1: int, x2: int, y2: int) -> None:
    """Sets graph mode, draws a line from (x1, y1) to (x2, y2) and returns to
    alpha mode"""
    sys.stdout.write(GS + coord(x1, y1) + coord(x2, y2) + US + CR)


def box(x1: int, y1: int, x2: int, y2: int) -> None:
    """Sets graph mode, draws a box from (x1, y1) to (x2, y2) and returns to
    alpha mode"""
    sys.stdout.write(
        GS
        + coord(x1, y1)
        + coord(x2, y1)
        + coord(x2, y2)
        + coord(x1, y2)
        + coord(x1, y1)
        + US
        + CR
    )
