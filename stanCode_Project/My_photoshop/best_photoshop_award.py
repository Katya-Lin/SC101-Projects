"""
File: best_photoshop_award.py
----------------------------------
This file creates a photoshopped image
that is going to compete for the 2020 Best
Photoshop Award for SC101P.
Please put all the images you use in image_contest folder
and make sure to choose which award you are aiming at
"""
from simpleimage import SimpleImage

# Controls the threshold of detecting green screen pixel
THRESHOLD = 1.2
# Controls the upper bound for black pixel
BLACK_PIXEL = 200

def main():  #主題:被巨貓吃掉之前的觀光客
    """
    TODO: Let the background pic replace the green screen of the figure pic.
    """
    fg = SimpleImage('image_contest/me.jpg')
    bg = SimpleImage('image_contest/back.jpg')
    bg.make_as_big_as(fg)
    combined_img = combine(bg, fg)
    combined_img.show()


def combine(bg,fg):
    for y in range(bg.height):
        for x in range(bg.width):
            pixel_fg = fg.get_pixel(x, y)
            avg = (pixel_fg.red+pixel_fg.blue+pixel_fg.green) // 3
            total = pixel_fg.red+pixel_fg.blue+pixel_fg.green
            if pixel_fg.green > avg*THRESHOLD and total > BLACK_PIXEL:
                pixel_bg = bg.get_pixel(x, y)
                pixel_fg.red = pixel_bg.red
                pixel_fg.blue = pixel_bg.blue
                pixel_fg.green = pixel_bg.green
    return fg

if __name__ == '__main__':
    main()
