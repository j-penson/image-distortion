#!/usr/bin/python
# coding=utf-8
""" Fixtures for Pytest Unit tests
:usage:
    Called by unit tests.
:authors
    JP at 09/01/20
"""

import pytest
from app.imaging import read_image, get_distortion_array


@pytest.fixture
def client():
    """Flask test client with Google Cloud logging client removed."""
    from main import create_app
    app = create_app()
    return app.test_client()


@pytest.fixture
def img_array():
    return read_image()


@pytest.fixture
def dist_array():
    return get_distortion_array()
