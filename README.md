# Vino Project Backend

<!-- Language Switcher - DO NOT EDIT THIS SECTION MANUALLY. It is automatically updated. -->
[English](README.md) | [Русский](README.ru.md)

<!-- END Language Switcher -->

## English

This is the backend service for the Vino project, built with FastAPI and utilizing JWT for authentication.

### Features

*   **JWT Authentication:** Secure user authentication and authorization using JSON Web Tokens.
*   **User Registration and Login:** Allows users to register and log in to the system.
*   **Token Refreshing:** Provides token refreshing mechanism to extend user sessions securely.
*   **Protected Routes:** Demonstrates how to protect routes using JWT authentication.
*   **Asynchronous Database Interaction:** Uses SQLAlchemy with asyncpg for asynchronous database operations.
*   **Dependency Injection:** Leverages FastAPI's dependency injection system for modular and testable code.
*   **Configuration with Pydantic:** Uses Pydantic for environment variable parsing and configuration management.
*   **Logging:** Implements structured logging for easier debugging and monitoring.
*   **Testing:** Includes comprehensive unit tests.

### Prerequisites

*   Python 3.13+
*   Docker (optional, for database)
*   A PostgreSQL database (can be local or remote)

### Installation

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd backend
    ```

2.  **Create and activate a virtual environment:**

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # Linux/macOS
    # .\.venv\Scripts\activate  # Windows
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r pyproject.toml
    ```

4.  **Set up the database:**

    *   Create a PostgreSQL database.  You can use Docker for this:

        ```bash
        docker run --name postgres -e POSTGRES_USER=root -e POSTGRES_PASSWORD=root -e POSTGRES_DB=db -p 5432:5432 postgres:latest
        ```

    *   Update the database connection settings in the `.env` file (create it if it doesn't exist):

        ```
        DB_TYPE=postgresql
        DB_HOST=localhost
        DB_PORT=5432
        DB_USER=root
        DB_PASSWORD=root
        DB_NAME=db
        ```

5.  **Run database migrations:**

    ```bash
    uv run alembic upgrade head
    ```

### Running the Application

1.  **Start the application:**

    ```bash
    uvicorn src.main:app --reload
    ```

    This will start the FastAPI application, and `--reload` enables automatic reloading on code changes.

### API Endpoints

*   `/api/v1/auth/token/` (POST):  Get JWT tokens (login).  Requires `login` and `password` in the request body.
*   `/api/v1/auth/register/` (POST): Register a new user. Requires `login` and `password` in the request body.
*   `/api/v1/auth/refresh/` (POST):  Refresh JWT tokens.  Requires a valid refresh token in a cookie.
*   `/api/v1/auth/protected` (GET): Protected endpoint (requires a valid access token in a cookie).

### Testing

1.  **Run unit tests:**

    ```bash
    uv run pytest
    ```

    or to see the coverage:
        ```bash
        uv run pytest --cov=./src
        ```

### Project Structure

```
backend/
├── src/
│   ├── api/
│   │   ├── __init__.py
│   │   ├── routes.py          # API router
│   │   └── v1/
│   │       ├── __init__.py
│   │       ├── depends.py      # Dependencies
│   │       ├── endpoints/
│   │       │   └── auth.py     # Authentication endpoints
│   │       └── routes.py      # Version 1 routes
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py          # Configuration settings
│   │   ├── general_constants.py
│   │   ├── logger/
│   │   │   ├── __init__.py
│   │   │   ├── filters.py      # Custom filters
│   │   │   └── logger.py      # Logger configuration
│   ├── db/
│   │   ├── __init__.py
│   │   ├── base_models.py     # Base model
│   │   ├── dependencies/
│   │   │   └── postgres_helper.py
│   │   └── models.py          # Database models
│   ├── domain/
│   │   ├── __init__.py
│   │   ├── entities/
│   │   │   ├── auth_master.py # Auth management
│   │   │   ├── token.py        # Token entities
│   │   │   └── user.py         # User entities
│   │   └── exceptions.py      # Custom exceptions
│   ├── main.py                # Main application entry point
│   ├── repository/
│   │   ├── __init__.py
│   │   ├── sql_queries/
│   │   │   ├── token_queries.py
│   │   │   └── user_queries.py
│   │   ├── token_repository.py # Token repository
│   │   └── user_repository.py  # User repository
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── token_schema.py    # Token schemas
│   │   └── user_schema.py     # User schemas
│   └── use_cases/
│       ├── __init__.py
│       ├── token_service.py   # Token service
│       └── user_service.py    # User service
├── tests/
│   ├── __init__.py
│   ├── conftest.py          # Pytest configurations
│   └── unit/
│       ├── __init__.py
│       ├── domain/
│       │   ├── __init__.py
│       │   ├── entities/
│       │   │   └── conftest.py
│       │   └── token_test.py
├── .env                     # Environment variables
├── .gitignore
├── alembic.ini              # Alembic configuration
├── Makefile                 # Makefile for common tasks
├── pyproject.toml           # Project dependencies
├── pytest.ini               # Pytest configuration
└── README.md                # This file
```

### Contributing

Contributions are welcome!  Please feel free to submit pull requests.

## Русский

Это бэкенд-сервис для проекта Vino, построенный с использованием FastAPI и использующий JWT для аутентификации.

### Функции

*   **JWT Аутентификация:** Безопасная аутентификация и авторизация пользователей с использованием JSON Web Tokens.
*   **Регистрация и вход пользователей:** Позволяет пользователям регистрироваться и входить в систему.
*   **Обновление токенов:** Предоставляет механизм обновления токенов для безопасного продления сеансов пользователей.
*   **Защищенные маршруты:** Демонстрирует, как защитить маршруты, используя JWT аутентификацию.
*   **Асинхронное взаимодействие с базой данных:** Использует SQLAlchemy с asyncpg для асинхронных операций с базой данных.
*   **Внедрение зависимостей:** Использует систему внедрения зависимостей FastAPI для модульного и тестируемого кода.
*   **Конфигурация с помощью Pydantic:** Использует Pydantic для парсинга переменных окружения и управления конфигурацией.
*   **Логирование:** Реализует структурированное логирование для упрощения отладки и мониторинга.
*   **Тестирование:** Включает в себя всесторонние модульные тесты.

### Необходимые условия

*   Python 3.13+
*   Docker (опционально, для базы данных)
*   База данных PostgreSQL (может быть локальной или удаленной)

### Установка

1.  **Клонируйте репозиторий:**

    ```bash
    git clone <repository_url>
    cd backend
    ```

2.  **Создайте и активируйте виртуальное окружение:**

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # Linux/macOS
    # .\.venv\Scripts\activate  # Windows
    ```

3.  **Установите зависимости:**

    ```bash
    pip install -r pyproject.toml
    ```

4.  **Настройте базу данных:**

    *   Создайте базу данных PostgreSQL. Для этого можно использовать Docker:

        ```bash
        docker run --name postgres -e POSTGRES_USER=root -e POSTGRES_PASSWORD=root -e POSTGRES_DB=db -p 5432:5432 postgres:latest
        ```

    *   Обновите параметры подключения к базе данных в файле `.env` (создайте его, если он не существует):

        ```
        DB_TYPE=postgresql
        DB_HOST=localhost
        DB_PORT=5432
        DB_USER=root
        DB_PASSWORD=root
        DB_NAME=db
        ```

5.  **Запустите миграции базы данных:**

    ```bash
    uv run alembic upgrade head
    ```

### Запуск приложения

1.  **Запустите приложение:**

    ```bash
    uvicorn src.main:app --reload
    ```

    Это запустит приложение FastAPI, а `--reload` включает автоматическую перезагрузку при изменениях кода.

### API Endpoints

*   `/api/v1/auth/token/` (POST): Получить JWT токены (вход). Требуется `login` и `password` в теле запроса.
*   `/api/v1/auth/register/` (POST): Зарегистрировать нового пользователя. Требуется `login` и `password` в теле запроса.
*   `/api/v1/auth/refresh/` (POST): Обновить JWT токены. Требуется действительный refresh token в cookie.
*   `/api/v1/auth/protected` (GET): Защищенная конечная точка (требуется действительный access token в cookie).

### Тестирование

1.  **Запустите модульные тесты:**

    ```bash
    uv run pytest
    ```
        или чтобы увидеть покрытие
        ```bash
        uv run pytest --cov=./src
        ```

### Структура проекта

```
backend/
├── src/
│   ├── api/
│   │   ├── __init__.py
│   │   ├── routes.py          # API роутер
│   │   └── v1/
│   │       ├── __init__.py
│   │       ├── depends.py      # Зависимости
│   │       ├── endpoints/
│   │       │   └── auth.py     # Конечные точки аутентификации
│   │       └── routes.py      # Маршруты версии 1
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py          # Настройки конфигурации
│   │   ├── general_constants.py
│   │   ├── logger/
│   │   │   ├── __init__.py
│   │   │   ├── filters.py      # Пользовательские фильтры
│   │   │   └── logger.py      # Настройка логирования
│   ├── db/
│   │   ├── __init__.py
│   │   ├── base_models.py     # Базовая модель
│   │   ├── dependencies/
│   │   │   └── postgres_helper.py
│   │   └── models.py          # Модели базы данных
│   ├── domain/
│   │   ├── __init__.py
│   │   ├── entities/
│   │   │   ├── auth_master.py # Управление аутентификацией
│   │   │   ├── token.py        # Сущности токенов
│   │   │   └── user.py         # Сущности пользователей
│   │   └── exceptions.py      # Пользовательские исключения
│   ├── main.py                # Главная точка входа в приложение
│   ├── repository/
│   │   ├── __init__.py
│   │   ├── sql_queries/
│   │   │   ├── token_queries.py
│   │   │   └── user_queries.py
│   │   ├── token_repository.py # Репозиторий токенов
│   │   └── user_repository.py  # Репозиторий пользователей
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── token_schema.py    # Схемы токенов
│   │   └── user_schema.py     # Схемы пользователей
│   └── use_cases/
│       ├── __init__.py
│       ├── token_service.py   # Сервис токенов
│       └── user_service.py    # Сервис пользователей
├── tests/
│   ├── __init__.py
│   ├── conftest.py          # Конфигурации Pytest
│   └── unit/
│       ├── __init__.py
│       ├── domain/
│       │   ├── __init__.py
│       │   ├── entities/
│       │   │   └── conftest.py
│       │   └── token_test.py
├── .env                     # Переменные окружения
├── .gitignore
├── alembic.ini              # Конфигурация Alembic
├── Makefile                 # Makefile для общих задач
├── pyproject.toml           # Зависимости проекта
├── pytest.ini               # Конфигурация Pytest
└── README.md                # Этот файл
```

### Вклад

Приветствуются любые предложения по улучшению!  Пожалуйста, отправляйте запросы на включение изменений (pull requests).