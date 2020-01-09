#!/usr/bin/python
# coding=utf-8
""" Tests for image distortion imaging functions
:usage:
    Run with every commit.
:authors
    JP at 09/01/20
"""
from app.imaging import distort_image
import numpy as np
from io import BytesIO


def test_read_image(img_array):
    """Check the read image is of the expected shape."""
    expected_shape = (200, 200, 3)
    actual_shape = img_array.shape
    assert expected_shape == actual_shape, f"Array shape not the expected {expected_shape}"
    assert np.max(img_array) <= 255, "Array contains values outside of expected 0-255 range"
    assert np.min(img_array) >= 0, "Array contains values outside of expected 0-255 range"


def test_get_distortion_array(dist_array):
    # TODO
    assert 1 == 1


def test_distort_image(img_array, dist_array):
    dist_img = distort_image(img_array, dist_array)
    assert isinstance(dist_img, BytesIO), "Expected a BytesIO image to be returned"
