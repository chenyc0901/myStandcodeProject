"""
File: blur.py
Name:
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors.
"""
"""
File: blur.py
Name:
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    blurred_img = SimpleImage.blank(img.width, img.height)  # To create the new image template

    for x in range(img.width):
        for y in range(img.height):
            # To set each color counter and number counter
            red_sum = green_sum = blue_sum = count = 0

            # To sum-up each color pixel around 3 X 3 region of (x, y) 
            for i in range(-1, 2):
                for j in range(-1, 2):
                    pixel_x = x + i
                    pixel_y = y + j
                    # only sum-up pixel within the figure range
                    if 0 <= pixel_x < img.width and 0 <= pixel_y < img.height:
                        neighbor_pixel = img.get_pixel(pixel_x, pixel_y)
                        red_sum += neighbor_pixel.red
                        green_sum += neighbor_pixel.green
                        blue_sum += neighbor_pixel.blue
                        count += 1
            # To calculate average pixel for each color and set to new image template
            new_pixel = blurred_img.get_pixel(x, y)
            new_pixel.red = red_sum // count
            new_pixel.green = green_sum // count
            new_pixel.blue = blue_sum // count
    return blurred_img


def main():
    """
    TODO:
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
