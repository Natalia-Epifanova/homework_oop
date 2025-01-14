# Работа над интернет магазином

## Цель проекта: 
Проект предназначен для:
+ описания основных сущностей и инициализации объектов



## Установка:
1. Клонируйте репозиторий:
```https://github.com/Natalia-Epifanova/homework_oop```
2. 2. Установите зависимости:
```pip install -r requirements.txt```


## Требования к проекту
- Python 3.11
- black 24.10.0
- flake8 7.1.1
- isort 5.13.2
- mypy 1.13.0
- pytest = 8.3.4
- pytest-cov = 6.0.0


## Реализованные функции и классы:
1. Модуль ```product```:
- Класс ```Product``` Для него определены следующие свойства: название (name),
описание (description), цена (price), количество в наличии (quantity).
2. Модуль ```category```:
- Класс ```Category``` Для него определены следующие свойства: название (name),
описание (description), цена (price), список товаров категории (products).
3. Модуль ```utils```:
- ```read_json_file``` Функция принимает на вход строку с указанием пути к файлу json, в котором хранится список с категориями, 
и возвращает список словарей с данными
- ```create_object_from_json``` Функция принимает на вход список словарей с категориями и преобразует эти данные в объекты


## Тестирование
Чтобы проверить процент покрытия кода тестами - необходимо:
- Ввести в терминале команду ```cd tests```
- Ввести в терминале команду ```poetry run pytest --cov-report term-missing --cov=src```
#### Благодаря тестам была осуществлена проверка всех функций на корректность работы. Было проверено:
- соответствие входных данных ожидаемым
- получение ожидаемого результата
- корректность работы функции при нестандартных входных данных (а именно выброс ошибок)
