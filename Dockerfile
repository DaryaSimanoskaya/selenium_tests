# Базовый образ Python
FROM python:3.11

# Обновление системы и установка зависимостей
RUN apt-get update && apt-get install -y \
    curl \
    unzip \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

# Установка необходимых Python-библиотек для тестов
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Копирование тестов в контейнер
COPY . /app
WORKDIR /app


COPY wait-for-it.sh /app/wait-for-it.sh
RUN chmod +x /app/wait-for-it.sh


# Установка Allure для генерации отчетов
RUN curl -o allure-2.17.3.tgz -L https://github.com/allure-framework/allure2/releases/download/2.17.3/allure-2.17.3.tgz \
    && tar -xvzf allure-2.17.3.tgz -C /opt/ \
    && ln -s /opt/allure-2.17.3/bin/allure /usr/local/bin/allure

# Установка переменных окружения
ENV EXECUTOR="host.docker.internal" \
    URL="http://localhost:8080" \
    BROWSER="chrome" \
    BROWSER_VERSION="128.0" \
    THREADS="1"

# Команда для запуска тестов через Selenoid
ENTRYPOINT ["sh", "-c", "/app/wait-for-it.sh opencart 8080 pytest --url=${URL} --browser=${BROWSER} --executor=${EXECUTOR} --browser-version=${BROWSER_VERSION} --threads=${THREADS} --remote --alluredir=./allure-results"]
