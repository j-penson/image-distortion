# image-distortion
Rest API using Flask, ImageIO and numpy to serve a logo with the left half distorted.

### Requirements
- Build an web application returning an image.
- Distort the left half of the image by subtracting 0-3 from the RGB values.
- The distortion should be different each time.

### API
**Method**|**Pattern**|**Action**
:-----:|:-----:|:-----:
GET|/v1/image and /|Return a version of the logo with distortion on the left side

### Local development
1. Create a virtual environment and install the requirements:
    ```bash
    python3 -m venv env
    . ./env/bin/activate
    pip install -r requirements.txt
    ```
2. Run tests
    `python3 -m pytest`
3. Run application
    `gunicorn main:app`
4. Build and run Docker image
    ```
   docker build -t image-distortion .
   docker run -it -p 8080:8080 image-distortion:latest
   ```


### TODO: with more time
- Distort different images
- Distort by amounts according to the request
- Swagger/OpenAPI documentation for the endpoint
- Performance profiling
- Deployment
- Security testing (e.g. https://github.com/zaproxy/zap-api-python)


### Commands run in a Github Action CI pipeline

flake8 style enforcement:

`flake8 --ignore=E203,C901,E402,E501,D400 --max-line-length=160 app/ test/ main.py`

Bandit security linting:

`bandit app.py`

Pytest unit tests:

`python3 -m pytest`