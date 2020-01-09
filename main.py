#!/usr/bin/python
# coding=utf-8
""" Image distortion application
:usage:
    Flask application.
:authors
    JP at 09/01/20
"""

from flask import Flask, send_file
from app.imaging import read_image, get_distortion_array, distort_image

# Create the Flask web application
app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def get_image():
    image = read_image()
    dist = get_distortion_array(distortion_amount=3)
    out = distort_image(image, dist)
    return send_file(out, mimetype='image/png')


def create_app():
    """Create the Flask application."""
    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
