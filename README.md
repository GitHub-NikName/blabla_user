
# blabla_user
Аудиозаписи пользователя.

Регистрация.
Принимает токен, id пользователя, медиафайл в формате wav.
Конвертирует в mp3, сохраняет бд, возвращает ссылку на скачивание формата 
http://127.0.0.1:8000/api/record?id=92&user=4

Данные бд хранятся на docker volume

## Технологии
- Python 3.11
- Django 3.2
- DRF 3.12
- Postgres 15.3
- Docker


## Как запустить проект:
- Клонировать репозиторий и перейти в него в командной строке:
```bash
$ git clone https://github.com/GitHub-NikName/blabla_user.git
$ cd blabla_user
```
- Скопировать и изменить настройки в .env
```bash
cp .env.exp .exp
````

```bash
$ docker-compose up -d --build
$ docker-compose exec web python manage.py migrate --noinput
````
перезапустить.  

## Пример запроса

POST-запрос с праметром `username` на эндпоинт `api/`

```json
{
  "username": "string"
}
```
Создает пользователя, возвращает его id, uuid

```json
{
    "id": "integer",
    "uuid": "string"
}
```

POST-запрос на эндпоинт `api/record/`

```json
{
  "user": "string",
  "token": "string",
  "file": "file upload"
}
```
Возвращает
```json
{
  "url": "string"
}
```
GET запрос по ссылке отдает файл на скачивание

### Контакты:

Сергеев Михаил  
[email](server-15@yandex.ru)  
[telegram](https://t.me/sergeev_mikhail)  
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
