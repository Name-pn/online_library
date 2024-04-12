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

|     **Переменная**    |           **Condition**          |                        **Effect**                        | **Effect, if condition is false**                                                           |
|:---------------------:|:--------------------------------:|:--------------------------------------------------------:|---------------------------------------------------------------------------------------------|
| MODE                  | "$MODE" == docker                | Change host of database postgres on one supported docker | Change host of database postgres on one supported default os which has postgres application |
| DEBUG                 | "$DEBUG" == True                 | DEBUG = True in settings Django                          | DEBUG = False in settings Django                                                            |
| LOAD_DEFAULT_DATABASE | "$LOAD_DEFAULT_DATABASE" == True | Load test data packet from db.json in database           | Switch off loading test data in database                                                    |