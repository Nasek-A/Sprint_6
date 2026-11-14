Автоматизированные UI-тесты сервиса [Яндекс Самокат](https://qa-scooter.praktikum-services.ru/) на Python, Selenium, Pytest и Allure.

## Структура проекта

```text
Sprint_6/
├── pages/                 # Page Object: действия на страницах
│   ├── base_page.py       # Общие действия и ожидания
│   ├── main_page.py       # Главная страница и FAQ
│   └── order_page.py      # Форма оформления заказа
├── tests/                 # Проверки пользовательских сценариев
│   ├── test_faq.py
│   ├── test_order.py
│   └── test_logo_navigation.py
├── data.py                # Тестовые данные и ожидаемые ответы FAQ
├── conftest.py            # Фикстура браузера
├── pytest.ini             # Настройки Pytest и Allure
└── requirements.txt       # Зависимости проекта
```

## Покрываемые сценарии

- Проверка ответов на все восемь вопросов FAQ.
- Оформление заказа с верхней и нижней кнопок, с двумя наборами данных.
- Возврат на главную страницу по логотипу Самоката.
- Открытие Дзена в новой вкладке по логотипу Яндекса.

## Установка

```bash
python -m venv .venv
```

Активация виртуального окружения в Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Установка зависимостей:

```bash
pip install -r requirements.txt
```

Для запуска тестов требуется установленный Firefox. Selenium Manager автоматически подбирает драйвер при наличии доступа к сети.

## Запуск тестов

Запуск всего набора:

```bash
pytest
```

Запуск отдельного файла:

```bash
pytest tests/test_order.py
```

Pytest сохраняет результаты Allure в `allure-results/` согласно настройкам `pytest.ini`.

## Формирование Allure-отчёта

После запуска тестов:

```bash
allure generate allure-results -o allure-report --clean
```

Открыть готовый отчёт:

```bash
allure open allure-report
```