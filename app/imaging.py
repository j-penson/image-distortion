#!/usr/bin/python
# coding=utf-8
""" Image manipulation
:usage:
    Called by Flask routes to read an image and distort it.
:authors
    JP at 09/01/20
"""

import imageio
import numpy as np
from io import BytesIO


def read_image(image_path: str = './images/logo.png') -> np.array:
    """Read an image and return an RGB numpy array.

    :param image_path: image location, default to Callsign logo.
    :return: m*n*3 numpy array representing the logo
    """
    im = imageio.imread(image_path, pilmode='RGB')
    return np.array(im)


def get_distortion_array(m: int = 200, n: int = 200, distortion_amount: int = 3) -> np.array:
    """Generate a random distortion for half an image size m/2*n*3. Concatenate to an array of zeros of the same size.

    :param m: width of image
    :param n: height of image
    :param distortion_amount: limit for distorting image
    :return: m*n*3 numpy array for distortion on half the image
    """
    half_width = int(n / 2)
    array_rand = np.random.randint(low=0, high=distortion_amount, size=(m, half_width, 3), dtype=np.uint8)
    array_zeros = np.zeros((m, half_width, 3), dtype=np.uint8)
    return np.concatenate((array_rand, array_zeros), axis=1)


def distort_image(image_array: np.array, distortion_array: np.array) -> BytesIO:
    """Combine the image and distortion arrays, check all values are positive and return the image.

    :param image_array: m*n*3 numpy array of original image
    :param distortion_array: m*n*3 distortion array
    :return:
    """
    # TODO split out into distort function and return function
    array_out = image_array - distortion_array
    array_out[array_out < 0] = 0
    img_bytes = imageio.imwrite('<bytes>', im=array_out, format='PNG')
    img = BytesIO(img_bytes)
    return img
