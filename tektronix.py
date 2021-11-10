GS = chr(29)
US = chr(31)
ESC = chr(27)
ETX = chr(3)
FF = chr(12)
CSI = ESC + "["


def tek_mode():
    "Enter Tektronix mode"
    print(CSI + "?38h")

def vt100_mode():
    "Goes back to VT100 mode"
    print(ESC + ETX)
        
def clear():
    "Clears the screen. On a real Tektronix, this flashes the screen white"
    print(ESC + FF)


def coord(x, y):
    "Translates coordinates to Tek strings"
    if x < 0 or x > 1024 or y < 0 or y > 768:
        raise ValueError("Invalid coordinates (%d, %d)" % (x, y))
    return chr(32 + (y // 32)) + chr(96 + (y & 31)) + chr(32 + x // 32) \
        + chr(64 + (x & 31))


def line(x1, y1, x2, y2):
    "Draws a line from *x1, y1) to (x2, y2)"
    print(GS + ESC + "[" + coord(x1, y1) + coord(x2, y2) + US)
