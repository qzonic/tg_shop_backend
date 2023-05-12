# Стек
<img src="https://img.shields.io/badge/Python-4169E1?style=for-the-badge"/> <img src="https://img.shields.io/badge/Django-008000?style=for-the-badge"/> <img src="https://img.shields.io/badge/DRF-800000?style=for-the-badge"/>

# Описание
### Проект PsutiShop

Проект представляет из себя бэкенд часть для телеграм магазина, в котором пользователи могут приобретать различные письменные работы.

### Как запустить проект:

*Клонировать репозиторий и перейти в него в командной строке:*
```
https://github.com/qzonic/tg_shop_backend.git
```
```
cd tg_shop_backend/
```

*Cоздать и активировать виртуальное окружение:*
```
python -m venv venv
```
* Windows
```
venv\Scripts\activate.bat
```
* Linux/MacOS.
```
source venv/bin/activate
```

*Установить зависимости из файла requirements.txt:*
```
pip install --upgrade pip
```

```
pip install -r requirements.txt
```

*Перейдите в директорию с файлом manage.py и выполните миграции:*
```
cd shop/
```

```
python manage.py makemigrations
```
```
python manage.py migrate
```

*Создать супер пользователя*
```
python manage.py createsuperuser
```

*Запустить проект:*
```
python manage.py runserver
```

### Автор
[![telegram](https://img.shields.io/badge/Telegram-Join-blue)](https://t.me/qzonic)
