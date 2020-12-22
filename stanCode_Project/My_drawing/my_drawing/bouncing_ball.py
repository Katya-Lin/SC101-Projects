"""
File: bouncing_ball.py
Name: Katya Lin
-------------------------
TODO: DROP THE BALL AND LET IT BOUNCE. THE BALL WILL BE AFFECTED BY THE GRAVITY. WHEN IT PASS THE RIGHT SIDE OF THE
      WINDOW, THE ANIME ENS, AND THE BALL WILL RETURN TO IT'S INITIAL SPOT.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 30
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
SWITCH = 0
COUNT = 0

window = GWindow(800, 500, title='bouncing_ball.py')
start = GOval(SIZE, SIZE, x=START_X, y=START_Y)
start.filled = True
start.fill_color = 'black'
window.add(start)

def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """

    onmouseclicked(drop)

def drop(mouse):

    global SWITCH, COUNT, START_X, START_Y
    if SWITCH == 0 and COUNT < 3:
        SWITCH = 1
        vy = 0
        COUNT += 1
        while True:
            start.move(VX, vy)
            vy += GRAVITY
            pause(DELAY)
            if start.y + SIZE >= window.height : # IF THE BALL HITS THE BOTTOM, IT TURNS TOWARD THE OPPOSITE DIRECTION
                vy *= -REDUCE


            if start.x - SIZE >= window.width:  # IF THE BALL HITS THE WALL, THE PROGRAM ENDS.
                start.x = START_X
                start.y = START_Y
                window.add(start)
                break

        SWITCH = 0

if __name__ == "__main__":
    main()
