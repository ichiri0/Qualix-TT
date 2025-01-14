# JSON-RPC Test Task

## Описание проекта

Это тестовое задание, реализующее функциональность для работы с JSON-RPC. В рамках проекта используется Django для серверной логики, а также взаимодействие с API через RPC-методы. Все взаимодействия с API осуществляются через HTTP-запросы с использованием JSON.

## Установка

### 1. Клонировать репозиторий

```bash
git clone <ссылка на репозиторий>
cd <папка проекта>
```

2. Создание и активация виртуального окружения (опционально)

```python3 -m venv .venv
source .venv/bin/activate  # Для Windows используйте .venv\Scripts\activate
```

3. Установка зависимостей

    ```pip install -r requirements.txt```

## Запуск проекта

### 1. Запуск через Docker

Для запуска проекта через Docker выполните следующие шаги:

	1.	Запустите контейнер:

```docker-compose up --build```


	3.	Приложение будет доступно на http://localhost:8000
    А само решение на http://localhost:8000/app/rpc_call

Примечание: Если у вас нет Docker, вы можете скачать и установить его с официального сайта.

    2. Запуск проекта без Docker
        1.	Убедитесь, что виртуальное окружение активировано (если вы используете его).
        2.	Примените миграции базы данных (опционально):

        ```python manage.py migrate```


	3.	Запустите сервер:

        ```python manage.py runserver```


	4.	Приложение будет доступно по адресу http://localhost:8000. http://localhost:8000/app/rpc_call

## Запуск тестов

1. Запуск тестов с использованием Django

Для запуска тестов используйте следующую команду:

```python manage.py test```

Тесты будут запущены, и результаты появятся в терминале.



### Примечания
•	Проект использует Django для серверной логики.

•	Для обработки JSON-RPC запросов в проекте используется стандартный подход с представлениями.

•	Весь код и взаимодействие с API осуществляется через HTTP-запросы.