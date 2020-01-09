#!/usr/bin/python
# coding=utf-8
""" Image distortion application
:usage:
    Flask application.
:authors
    JP at 09/01/20
"""

from flask import Flask, send_file
from app.imaging import read_image, get_distortion_array, combine_distort_array, convert_distorted_image

# Create the Flask web application
app = Flask(__name__)


@app.route('/v1/image', methods=["GET"])
@app.route('/', methods=["GET"])
def get_image():
    image = read_image('./images/logo.png')
    dist = get_distortion_array(distortion_amount=3)
    dist_img_array = combine_distort_array(image, dist)
    out = convert_distorted_image(dist_img_array)
    return send_file(out, mimetype='image/png')


def create_app():
    """Create the Flask application."""
    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
