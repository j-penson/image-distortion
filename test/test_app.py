#!/usr/bin/python
# coding=utf-8
""" Tests for image distortion Flask application
:usage:
    Run with every commit.
:authors
    JP at 09/01/20
"""


def test_index(client):
    """Check the index page loads."""
    response = client.get('/')
    assert response.status_code == 200
