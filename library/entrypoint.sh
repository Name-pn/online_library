#!/bin/sh

python manage.py migrate
#python -Xutf8 manage.py loaddata db.json
#python manage.py collectstatic --noinput

exec "$@"