"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120  # 120 frames per second.
NUM_LIVES = 3


def main():

    graphics = BreakoutGraphics()
    # Add animation loop here!
    global NUM_LIVES


    while True:


        pause(FRAME_RATE)

        graphics.ball.move(graphics.get_dx(), graphics.get_dy())

        if graphics.ball.y >= graphics.window.height:
            NUM_LIVES -= 1
            if NUM_LIVES == 2:
                graphics.window.remove(graphics.live_3)
            if NUM_LIVES == 1:
                graphics.window.remove(graphics.live_2)

            if NUM_LIVES > 0:
                graphics.reset_ball()
                graphics.reset_dx()
                graphics.reset_dy()
                graphics.switch = 0
            else:
                graphics.window.remove(graphics.live_1)
                graphics.window.add(graphics.label_e)
                break

        if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
            graphics.change_dx()

        if graphics.ball.y <= 0:
            graphics.change_dy()

        obj = graphics.object()
        if obj is not None:
            graphics.b_or_p()




if __name__ == '__main__':
    main()
