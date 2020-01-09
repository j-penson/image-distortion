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
    im_array = np.array(im)
    return im_array


def get_distortion_array(m: int = 200, n: int = 200, distortion_amount: int = 3) -> np.array:
    """Generate a random distortion for half an image size m/2*n*3. Concatenate to an array of zeros of the same size.

    :param m: width of image
    :param n: height of image
    :param distortion_amount: limit for distorting image
    :return: m*n*3 numpy array for distortion on half the image
    """
    half_width = int(n / 2)
    array_rand = np.random.randint(low=0, high=distortion_amount+1, size=(m, half_width, 3), dtype=np.uint8)
    array_zeros = np.zeros((m, half_width, 3), dtype=np.uint8)
    return np.concatenate((array_rand, array_zeros), axis=1)


def combine_distort_array(image_array: np.array, distortion_array: np.array) -> np.array:
    """Combine the image and distortion arrays, convert all values to a positive value and return the array.

    :param image_array: m*n*3 numpy array of original image
    :param distortion_array: m*n*3 distortion array
    :return: array of distorted image
    """
    img_dist_array = image_array - distortion_array
    img_dist_array[img_dist_array < 0] = 0
    return img_dist_array


def convert_distorted_image(dist_img_out: np.array) -> BytesIO:
    """Convert the distorted array to a image for serving

    :param dist_img_out: array of distorted image
    :return: BytesIO stream of image
    """
    img_bytes = imageio.imwrite('<bytes>', im=dist_img_out, format='PNG')
    img = BytesIO(img_bytes)
    return img
