# Тестовые задание и групповые работы для AI LEARNING WEEK 2025 в Красноярске

Простой репозиторий с наработками и доп информацией в рамках интенсива AI LEARNING WEEK 2025.

[Подробный отчет](./test_task/REPORT.md)  
[Реализация тестового задания](./test_task/task.py)  
[Описание групповых работ]()

## Быстрый старт

1. Установка сертификата минцифры для работы GigaChat  

``` bash
    curl -k "https://gu-st.ru/content/lending/russian_trusted_root_ca_pem.crt" -w "\n" >> "$(python3 -c "import certifi; print(certifi.where())")"
```

2. Установка ключей в файл переменных среды .env (`GEMINI_API_KEY`, `GIGACHAT_API_KEY`, `PROXY_URL`)

3. Создание виртуальной среды и установка зависимостей

``` bash
    python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt
```

4. Запуск проекта с тестовыми заданиями

``` bash
    python3 ./test_task/task.py
```