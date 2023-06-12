"""
File: stanCodoshop.py
Name: 
----------------------------------------------
SC101_Assignment3 Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns a value that refers to the "color distance" between a pixel and a mean RGB value.

    Input:
        pixel (Pixel): the pixel with RGB values to be compared
        red (int): the average red value of the pixels to be compared
        green (int): the average green value of the pixels to be compared
        blue (int): the average blue value of the pixels to be compared

    Returns:
        dist (float): the "color distance" of a pixel to the average RGB value of the pixels to be compared.
    """
    color_distance_square = (red - pixel.red) ** 2 + (green - pixel.green) ** 2 + (blue - pixel.blue) ** 2
    color_distance = pow(color_distance_square, 0.5)
    return color_distance


def get_average(pixels):
    """
    Given a list of pixels, finds their average red, blue, and green values.

    Input:
        pixels (List[Pixel]): a list of pixels to be averaged

    Returns:
        rgb (List[int]): a list of average red, green, and blue values of the pixels
                        (returns in order: [red, green, blue])
    """
    red_avg = sum([obj.red for obj in pixels]) / len(pixels)
    green_avg = sum([obj.green for obj in pixels]) / len(pixels)
    blue_avg = sum([obj.blue for obj in pixels]) / len(pixels)
    return [red_avg, green_avg, blue_avg]


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest "color distance", which has the closest color to the average.

    Input:
        pixels (List[Pixel]): a list of pixels to be compared
    Returns:
        best (Pixel): the pixel which has the closest color to the average
    """
    red_avg, green_avg, blue_avg = get_average(pixels)
    # To get obj:distance pairs
    distance_array = {obj: get_pixel_dist(obj, red_avg, green_avg, blue_avg) for obj in pixels}
    min_pixel_obj, min_distance = sorted(distance_array.items(), key=lambda obj: obj[1])[0]
    # solution 2
    # distance_array = [get_pixel_dist(obj, red_avg, green_avg, blue_avg) for obj in pixels]
    # min_pixel = min(distance_array)
    # min_pixel_index = distance_array.index(min_pixel)
    # return pixels[min_pixel_index]
    return min_pixel_obj

def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)

    # ----- YOUR CODE STARTS HERE ----- #
    # Write code to populate image and create the 'ghost' effect
    for x in range(width):
        for y in range(height):
            pixels = [img.get_pixel(x, y) for img in images]
            best_pixel = get_best_pixel(pixels)
            result_figure = result.get_pixel(x, y)
            result_figure.red = best_pixel.red
            result_figure.green = best_pixel.green
            result_figure.blue = best_pixel.blue

    # ----- YOUR CODE ENDS HERE ----- #

    print('Displaying image!')
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
