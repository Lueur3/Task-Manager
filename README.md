# Task Manager (CLI)

A simple task management system built using Object-Oriented Programming (OOP) principles and persistent JSON storage.

## Features

- Create tasks with a title and description.
- Update task completion status.
- Remove tasks from the list.
- View a summary of all tasks and detailed information for a specific task index.
- Automatic data saving and loading from `data/tasks.json`.
- Index validation and input error handling.

## Project Structure

- `models.py`: Contains `Task` (individual task model) and `ToDoList` (task list management container) classes.
- `storage.py`: Logic for data persistence (JSON serialization and deserialization of objects).
- `main.py`: Command-line interface and module coordination.
- `tests/`: Unit tests for verifying class logic and methods.

## Installation and Execution (Local)

1.  **Install dependencies**:

    ```bash
    pip install pytest
    ```

2.  **Run the application**:

    ```bash
    python src/main.py
    ```

3.  **Run tests**:
    ```bash
    pytest tests/test_models.py
    ```

## Running with Docker

1.  **Build the image**:

    ```bash
    docker build -t task-manager .
    ```

2.  **Run the container**:
    ```bash
    docker run -it -v "$(pwd)/data:/app/data" task-manager:latest
    ```
    _The `-v` flag ensures the `tasks.json` file is persisted on the host machine._

---

# Менеджер задач (CLI)

Простейший менеджер задач, реализованный на принципах объектно-ориентированного программирования с постоянным хранением данных в формате JSON.

## Функционал

- Создание задач с указанием названия и описания.
- Изменение статуса выполнения задачи.
- Удаление задач из списка.
- Просмотр краткого списка всех задач и детальной информации по конкретному индексу.
- Автоматическое сохранение изменений и загрузка данных из файла `data/tasks.json`.
- Валидация индексов и обработка некорректного ввода.

## Структура проекта

- `models.py`: Содержит классы `Task` (модель отдельной задачи) и `ToDoList` (контейнер для управления списком задач).
- `storage.py`: Модуль для обеспечения постоянного хранения данных (сериализация и десериализация объектов в JSON).
- `main.py`: Интерфейс командной строки и координация работы модулей.
- `tests/`: Модульные тесты для проверки логики классов и методов.

## Установка и запуск (Локально)

1.  **Установка зависимостей**:

    ```bash
    pip install pytest
    ```

2.  **Запуск приложения**:

    ```bash
    python src/main.py
    ```

3.  **Запуск тестов**:
    ```bash
    pytest tests/test_models.py
    ```

## Запуск через Docker

1.  **Сборка образа**:

    ```bash
    docker build -t task-manager .
    ```

2.  **Запуск контейнера**:
    ```bash
    docker run -it -v "$(pwd)/data:/app/data" task-manager:latest
    ```
    _Флаг `-v` обеспечивает сохранение файла `tasks.json` на хост-машине._
