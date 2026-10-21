# QR Code Generator in Docker

A Python program that turns a URL into a QR code PNG, packaged as a Docker
image that runs as a non-root user.

## Build and run

    docker build -t qr-code-generator-app .
    mkdir -p qr_codes
    docker run --rm -v "$PWD/qr_codes:/app/qr_codes" qr-code-generator-app --url https://www.njit.edu

The PNG is written to the qr_codes folder on your machine with a timestamped
name. Create the folder before running, so it is owned by you and not by
Docker, otherwise the container cannot write to it.

## Configuration

Optional environment variables, passed with -e:

- QR_CODE_DIR: output folder, default qr_codes
- FILL_COLOR: QR color, default red
- BACK_COLOR: background color, default white

## Image

https://hub.docker.com/r/chima765432/is601-qr-code-generator-app

## Tests

    pip install -r requirements.txt pytest
    pytest

GitHub Actions runs the tests, then builds the image and runs the container
to confirm a QR code file is actually produced.
