# scrapy_parser_pep
Парсер документов PEP на базе фреймворка Scrapy.
Парсер вывод собранную информацию в два файла .csv:
В первый файл выводится список всех PEP: номер, название и статус.
Второй файл содержит сводку по статусам PEP — сколько найдено документов в каждом статусе (статус, количество).

## Запуск проекта
Клонируйте проект

```git clone git@github.com:<> ```

Создание виртуального окружения

```python -m venv venv ```

Активация виртуального окружения

```source venv/Scripts/activate ```

Обновляем pip

```python -m pip install --upgrade pip ```

Установка пакетов по файлу

```pip install -r requirements.txt ```

Старт проекта

``` scrapy startproject pep_parse .```

Создание паука

```scrapy genspider pep peps.python.org ```

## Запуск парсера

```scrapy crawl pep ``` 

Автор проекта https://github.com/Kate1109

