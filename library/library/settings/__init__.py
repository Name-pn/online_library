from split_settings.tools import include
import dotenv
import os

# Подгружаем переменные окружения
dotenv.load_dotenv()

# Подгружаем базовые настройки
include('base.py')

if os.environ.get('MODE') == "prod":
    include('production.py')

if os.environ.get('MODE') == "docker":
    include('docker.py')