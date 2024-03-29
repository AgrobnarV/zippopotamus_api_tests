# API Testing with pytest

This project contains smoke tests for the API endpoint that provides location information based on postal codes.

## Prerequisites
- Docker installed on your machine

## Usage

1. Clone this repository (git clone)

2. Navigate to the project directory (cd project)

3. Build the Docker image (docker build -t api-tests )

4. Run the Docker container with volumes mapped to save report.html to your host machine:

    ```
    docker run -v $(pwd)/reports:/app/reports api-tests
    ```
   This command maps the `/app/reports` directory in the container to the `reports` directory in your current working directory on the host machine. 
   So, the report.html file generated by tests will be saved to the `reports` directory on your host machine.

5. Once the tests are finished, you can find the report.html file in the `reports` directory.

## Test Endpoint

The API endpoint to be tested is https://api.zippopotam.us/#who.

## Test Scenarios Covered

- Smoke testing for the API endpoint GET https://api.zippopotam.us/{country}/{postal-code}

