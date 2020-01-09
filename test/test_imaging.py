#!/usr/bin/python
# coding=utf-8
""" Tests for image distortion imaging functions
:usage:
    Run with every commit.
:authors
    JP at 09/01/20
"""
from app.imaging import combine_distort_array, convert_distorted_image
import numpy as np
from io import BytesIO


def test_read_image(img_array):
    """Check the read image is of the expected shape."""
    expected_shape = (200, 200, 3)
    actual_shape = img_array.shape
    assert expected_shape == actual_shape, f"Array shape not the expected {expected_shape}"
    assert np.max(img_array) <= 255, "Array contains values outside of expected 0-255 range"
    assert np.min(img_array) >= 0, "Array contains values outside of expected 0-255 range"


def test_get_distortion_array_zeros(dist_array):
    """Test the right half of the image array is of sum zero."""
    split_array = np.hsplit(dist_array, 2)
    zeros_array = np.sum(split_array[1])
    expected = 0
    actual = np.sum(zeros_array)
    assert expected == actual, f"expecting sum of array to be 0"


def test_get_distortion_array_random(dist_array):
    """Test the right half of the image array is of sum zero."""
    split_array = np.hsplit(dist_array, 2)
    dist_half_array = split_array[0]
    assert np.max(dist_half_array) == 3, "Expecting the dist array to contain a 3"
    assert np.min(dist_half_array) == 0, "Expecting the dist array to contain a 0"


def test_combine_distort_array(img_array, dist_array):
    """Check the sum of the combined array is less that or equal to the sum of the image array minus the dist array."""
    expected = np.sum(img_array) - np.sum(dist_array)
    img_dist_array = combine_distort_array(img_array, dist_array)
    actual = np.sum(img_dist_array)
    if np.min(img_array) >= 3:
        assert expected == actual, "Array size not equal as expected"
    else:
        assert expected > actual, "Array size not smaller as expected"


def test_convert_distorted_image(img_array):
    """Check the type of the image after conversion"""
    return_image = convert_distorted_image(img_array)
    assert isinstance(return_image, BytesIO), "Expected a BytesIO image to be returned"
