### Описание проекта:

В репозитории - проект API для Yatube, с реализованным API для всех моделей приложения. 

### Технологии

Python 3.7

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

Cоздать и активировать виртуальное окружение:

```
python -m venv env
```

```
source venv/scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py makemigrations
```

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

### Примеры запросов

Авторизированному пользователю необходимо получить токен, для этого нужно выполнить POST-запрос /api/v1/jwt/create/ передав поля username и password созданного пользователя.

При отправке запроса авторизированного пользователя передайте токен в заголовке Authorization: Bearer <токен>

/api/v1/posts/ (GET, POST, PUT, PATCH, DELETE)

/api/v1/posts/{post_id}/comments/ (GET, POST, PUT, PATCH, DELETE)

/api/v1/groups/ (GET)

/api/v1/follow/ (GET, POST)

### Авторы

Артём, под чутким руководством наставников Яндекс практикума