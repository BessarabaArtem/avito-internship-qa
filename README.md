Тестовое задание Avito (QA Internship)

Привет!
Это репозиторий с моим решением тестового задания на позицию QA-стажера.
Все задания выполнены и находятся в корневой папке проекта.
Надеюсь мое решение вам понравится)

Структура проекта

```
avito-internship-qa/
├── REPORTS.md          # Таблица с багами (Задание 1)
├── Site_bugs.png       # Скриншот с ошибками
├── TESTCASES.md        # Список тест-кейсов (Задание 2)
├── test_api.py         # Код автотестов
├── .gitignore          # Настройки Git
└── README.md           # Эта инструкция
```

1. Задание 1: Поиск багов (UI)

Я провел ручное тестирование интерфейса поиска вакансий.

· REPORTS.md — таблица с описанием найденных багов и их приоритетом.
· Site_bugs.png — скриншот с визуализацией ошибок.

2. Задание 2: Тестирование API

Автоматизация проверок микросервиса объявлений.

· TESTCASES.md — план тестирования (список проверок).
· .gitignore — конфигурация для исключения лишних файлов.
· test_api.py — код автотестов (Python + Pytest).
· BUGS.md — отчет о багах, найденных в API (будет создан после прогона тестов).

---

Стек технологий

· Документация: Markdown
· Автотесты: Python, Pytest, Requests
· Инструменты: Git, VS Code

---

Как запустить тесты

Предварительно: Убедитесь, что установлен Python.

1. Клонируйте репозиторий
   ```bash
   git clone https://github.com/BessarabaArtem/avito-internship-qa.git
   ```
2. Установка зависимостей
   ```bash
   pip install pytest requests
   ```
3. Запуск проверок
   ```bash
   pytest -v test_api.py
   ```

---

Результаты тестирования

```
test_api.py::test_create_item PASSED                                [ 16%]
test_api.py::test_get_item PASSED                                   [ 33%]
test_api.py::test_get_seller_items PASSED                           [ 50%]
test_api.py::test_get_statistic PASSED                              [ 66%]
test_api.py::test_create_item_invalid_price PASSED                  [ 83%]
test_api.py::test_get_nonexistent_item PASSED                       [100%]

======================== 6 passed in 2.54s =========================
```

---

Технические детали

```
Язык: Python 3.x
Фреймворк: Pytest
HTTP-клиент: Requests
Target API: https://qa-internship.avito.com
```

---

Решение проблем

Ошибка: "pytest не найден"

```bash
pip install pytest
```

Ошибка: "ModuleNotFoundError"

```bash
pip install pytest
```

---

Автор

Бессараба Артём, кандидат QA Engineer Avito
