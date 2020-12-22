"""
File: draw_line.py
Name: Katya Lin
-------------------------
TODO: CLICK ON THE WINDOW TO CREATE A CIRCLE AS START, CLICK AGAIN AS END, USE THE START AND THE END TO CREATE A LINE.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

window = GWindow()
SIZE = 10
click = 0
START_X = 0
START_Y = 0
start = 0



def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(S_and_E)

def S_and_E(e):


    global click
    global location
    global start
    global START_X
    global START_Y
    global END_X
    global END_Y

    if click%2 == 0 :
        start = GOval(SIZE, SIZE, x = e.x-(SIZE/2), y = e.y-(SIZE/2))
        window.add(start)
        START_X = e.x
        START_Y = e.y
        click += 1
    else:
        window.remove(start)
        line = GLine(START_X, START_Y, e.x, e.y)
        window.add(line)
        click = 0


if __name__ == "__main__":
    main()
