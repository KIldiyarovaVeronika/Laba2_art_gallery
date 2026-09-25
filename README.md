# Онлайн-галерея произведений искусств (Lab2_RV)

## Описание

Проект на DJango - онлайн-галерея произведений искусств. 
Реализовано сохранение пользовательских настроек (тема оформления, 
размер шрифта, последняя посещённая страница) через cookies.

## Функционал

- Отображение галереи картин (данные хранятся в виде списка словарей в `views.py`).
- HTML-форма для выбора темы оформления (светлая/тёмная) и размера шрифта.
- Сохранение настроек пользователя в cookies браузера.
- Внешняя таблица стилей (`style.css`) — тёмная и светлая темы.
- Статические файлы (изображения картин).

## Структура проекта
```
lab2_RV/
├── .venv/                  # виртуальное окружение (в .gitignore)
├── .gitignore
├── README.md
├── requirements.txt
└── art_gallery/            # Django-проект
    ├── manage.py
    ├── myproject/          # настройки проекта
    └── myapp/              # приложение галереи
        ├── templates/myapp/gallery.html
        ├── static/myapp/css/style.css
        ├── static/myapp/images/
        ├── forms.py
        ├── urls.py
        └── views.py
```

## Технологии

- Python 3.14
- Django 6.1
- HTML5, CSS3
- Cookies (для сохранения настроек)

## Установка и запуск

### 1. Клонировать репозиторий

```bash
git clone <ссылка_на_ваш_репозиторий>
cd lab2_RV
```

### 2. Создать и активировать виртуальное окружение

```bash
python -m venv .venv

# Windows:
.venv\Scripts\activate

# Mac / Linux:
source .venv/bin/activate
```
### 3. Установить зависимости

```bash
pip install -r requirements.txt
```
### 4. Применить миграции

```bash
cd art_gallery
python manage.py migrate
```
###  5. Запустить сервер разработки

```bash
python manage.py runserver
```
### 6. Открыть в браузере
http://127.0.0.1:8000/