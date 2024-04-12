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
For run application on your os and dont get error message. But you need install all requirements from requirements.txt or library/requirements.txt for your python venv.

You also can swith on DEBUG mode setting value True for DEBUG var in .env

Next you can use loading default database from library/db.json when you set LOAD_DEFAULT_DATABASE var value to "True"