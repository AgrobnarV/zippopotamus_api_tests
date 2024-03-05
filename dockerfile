FROM python:3.10
WORKDIR /app
COPY . .
RUN pip install requirements.txt
CMD ["pytest", "test_api_zippopotam.py", "test_performance.py", "test_response_data.py", "test_status_code.py"]

