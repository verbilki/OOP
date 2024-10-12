## Объектно-ориентированное программирование

Этот проект представляет собой Домашнее задание по уроку 14.1 (блок '4. Объектно-ориентированное программирование')
курса по Python на платформе SkyPro
ученика Олега Жадана (поток Prof 40.0).

## Инструкция по установке

SSH-ссылка для клонирования проекта с Github:

```
git@github.com:verbilki/OOP.git
```

Создать в PyCharm виртуальное окружение

### Для Windows

```commandline
python -m venv venv
```

### Для Linux, macOS

```bash
python3 -m venv venv
```

Активировать виртуальное окружение
Следующую команду следует запускать из корня проекта:

### Для Windows

```commandline
venv\Scripts\activate
```

#### Для Linux, macOS

```bash
source ./venv/bin/activate
```

Установить Poetry.

```bash
poetry install
```

Установить линтер flake8, анализатор статического кода mypy, форматтеры (black, isort)
на основании файла конфигурации pyproject.toml.

Пример настройки flake8, black, isort и mypy в файле pyproject.toml:

```
[tool.poetry.dependencies]
   python = "^3.8"
   flake8 = "^3.8.4"
   black = "^20.8b1"
   isort = "^5.6.4"
   mypy = "^0.790"
```

Установить в терминале дополнительные пакеты:

Если в файле pyproject.toml отсутствуют записи о пакетах requests и python-dotenv,
то их необходимо установить из терминала:

```bash
poetry add requests
poetry add python-dotenv

pip install pandas pandas-stubs openpyxl numpy types-requests
```

### Запуск приложения

Для запуска приложения необходимо запустить на исполнение модуль src/main.py, состоящий из единственной функции main().

### Настройка и использование фреймворка unit-тестирования Pytest

Исходный код модулей покрыт юнит-тестами Pytest на более, чем 80%. Для запуска выполните команды:

```bash
poetry add --group dev pytest # установка pytest в виртуальное окружение приложения
pytest # запуск тестов
```

Команда для формирования HTML-отчёта в терминале:

```bash
pytest --cov=src --cov-report=html
```

В результате зтого запуска будет сформирован HTML-отчет (файл htmlcov/index.html) о покрытии тестами.

### Лицензия

[GPL 3.0](https://www.gnu.org/licenses/gpl-3.0.html#license-text)