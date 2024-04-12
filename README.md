# Backend for web library
## Requirements
- Installed Docker
- For running in your os python.

## Installation
1. Rename ".env.example" file to ".env"
2. In cmd on Windows or other shell use command
```bash
docker-compose build
docker-compose up
```
3. In your browser in your browser go to "localhost:8001". You will see message from the site.
## What you may next
1. You can go to "localhost:8001/api/docs" for knowing swager. 
2. You can go to "localhost:8001/admin" for knowing admin of django web-site.
3. You can send request to API
## About .env file
You can change some settings when you change .env file.
Default value docker of mode var telling us that we use docker, but you can change it to "none" and then you can use 
```bash
python library/manage.py runserver 8001
```
Table with .env vars below

|     **Переменная**    |            **Условие**           |                                **Действие**                               | **Действие если условие не выполнено**                                                                                 |
|:---------------------:|:--------------------------------:|:-------------------------------------------------------------------------:|------------------------------------------------------------------------------------------------------------------------|
| MODE                  | "$MODE" == docker                | Изменяет хост базы данных postgres на тот, который поддерживается докером | Хост базы данных остается localhost, что означает возможность запуска сервера на локальном компьютере через manage.py  |
| DEBUG                 | "$DEBUG" == True                 | DEBUG = True в настройках Django                                          | DEBUG = False в настройках Django                                                                                      |
| LOAD_DEFAULT_DATABASE | "$LOAD_DEFAULT_DATABASE" == True | Загружает тестовый пакет данных из db.json в базу данных                  | Отключает загрузку тестовых данных в БД                                                                                | 