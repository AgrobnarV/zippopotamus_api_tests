FROM python:3.10
WORKDIR /app

# Установка зависимостей
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копирование остальных файлов
COPY . .

# Запуск тестов и генерация report.html
CMD ["pytest", "--html=report.html", "test_api_zippopotam.py", "test_performance.py", "test_response_data.py", "test_status_code.py"]
