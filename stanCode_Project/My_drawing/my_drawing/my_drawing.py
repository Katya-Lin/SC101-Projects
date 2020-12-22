"""
File: my_drawing.py
Name: Katya Lin
----------------------
TODO:This file uses campy module to draw a anime character named Tamama
"""

from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.graphics.gwindow import GWindow


def main():
    """
    TODO: We use GOval, GRect and GLabel to draw.
    """
    window = GWindow(width=600, height=700)

    hat = GOval(210, 210, x=180, y=100)
    hat.filled = True
    hat.fill_color = 'khaki'
    hat.color = 'khaki'
    window.add(hat)

    hat_r = GOval(90, 180, x=165, y=150)  # right side of the hat
    hat_r.filled = True
    hat_r.fill_color = 'khaki'
    hat_r.color = 'khaki'
    window.add(hat_r)

    hat_l = GOval(90, 180, x=315, y=150)  # left side of the hat
    hat_l.filled = True
    hat_l.fill_color = 'khaki'
    hat_l.color = 'khaki'
    window.add(hat_l)

    face_b = GOval(170, 160, x=200, y=150) # black part of the face
    face_b.filled = True
    face_b.fill_color = 'midnightblue'
    face_b.color = 'midnightblue'
    window.add(face_b)

    body = GOval(100, 200, x=240, y=270)
    body.filled = True
    body.fill_color = 'midnightblue'
    body.color = 'midnightblue'
    window.add(body)

    body_w = GOval(70, 130, x=255, y=315) # The white part of the body
    body_w.filled = True
    body_w.fill_color = 'white'
    body_w.color = 'white'
    window.add(body_w)

    sign_r = GRect(25, 30, x=263, y=360)
    sign_r.filled = True
    sign_r.fill_color = 'yellow'
    window.add(sign_r)

    sign_l = GRect(25, 30, x=287, y=360)
    sign_l.filled = True
    sign_l.fill_color = 'green'
    window.add(sign_l)

    arm_r = GOval(135, 20, x=127, y=330)
    arm_r.filled = True
    arm_r.fill_color = 'midnightblue'
    arm_r.color = 'midnightblue'
    window.add(arm_r)

    arm_l = GOval(135, 20, x=324, y=330)
    arm_l.filled = True
    arm_l.fill_color = 'midnightblue'
    arm_l.color = 'midnightblue'
    window.add(arm_l)

    leg_r = GOval(20, 135, x=260, y=445)
    leg_r.filled = True
    leg_r.fill_color = 'midnightblue'
    leg_r.color = 'midnightblue'
    window.add(leg_r)

    leg_l = GOval(20, 135, x=300, y=445)
    leg_l.filled = True
    leg_l.fill_color = 'midnightblue'
    leg_l.color = 'midnightblue'
    window.add(leg_l)

    face_w = GOval(140, 120, x=217, y=190)
    face_w.filled = True
    face_w.fill_color = 'white'
    face_w.color = 'white'
    window.add(face_w)

    eye_wr = GOval(65, 65, x=217, y=190)
    eye_wr.filled = True
    eye_wr.fill_color = 'white'
    eye_wr.color = 'black'
    window.add(eye_wr)

    eye_wl = GOval(65, 65, x=300, y=190)
    eye_wl.filled = True
    eye_wl.fill_color = 'white'
    eye_wl.color = 'black'
    window.add(eye_wl)

    eye_br = GOval(50, 50, x=232, y=199)
    eye_br.filled = True
    eye_br.fill_color = 'black'
    eye_br.color = 'black'
    window.add(eye_br)

    eye_bl = GOval(50, 50, x=301, y=199)
    eye_bl.filled = True
    eye_bl.fill_color = 'black'
    eye_bl.color = 'black'
    window.add(eye_bl)

    eye_rr = GOval(30, 30, x=250, y=210)  # reflection of the right eye
    eye_rr.filled = True
    eye_rr.fill_color = 'white'
    eye_rr.color = 'white'
    window.add(eye_rr)

    eye_rl = GOval(30, 30, x=301, y=210)  # reflection of the left eye
    eye_rl.filled = True
    eye_rl.fill_color = 'white'
    eye_rl.color = 'white'
    window.add(eye_rl)

    mouth = GRect(50, 25, x=263, y=268)
    mouth.filled = True
    mouth.fill_color = 'tomato'
    mouth.color = 'tomato'
    window.add(mouth)

    name = GLabel('TAMAMA', x=260, y=147)
    name.font = '-10'
    name.color = 'red'
    window.add(name)


if __name__ == '__main__':
    main()
