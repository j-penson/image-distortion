# image-distortion

Rest API to serve a logo with the left half distorted.

### Requirements
- Build a Python app exposing an HTTP endpoint that returns an image (attached)
- The left half of the image should have random distortion applied to each pixel.
- The distortion effect should be such that the red, green and blue components of each pixels are between n-3 and n where n is the original integer representation of the pixel’s colour component. 
- Different distortion should be applied (and therefore slightly different picture served) each time you call the endpoint.
- Include unit and integration tests as you think is necessary.
- Limit the above to 2hrs.



# TODO
- write tests for image manipulation
- add github action
- add api versioning
- add swagger docs

# TODO with more time
- API endpoint versioning
- Swagger documentation
- Performance testing
- Security testing (e.g. https://github.com/zaproxy/zap-api-python)


### Commands run in a CI pipeline

flake8 style enforcement:

`flake8 --ignore=E203,C901,E402,E501,D400 --max-line-length=160 app/ test/ main.py`

Bandit security linting:

`bandit app.py`

Pytest unit tests with 80% minimum coverage:

`python3 -m pytest --cov=src --cov-fail-under=80`