#!/bin/sh

python manage.py migrate
if [[ "$LOAD_DEFAULT_DATABASE" == "True" ]]
then
  python -Xutf8 manage.py loaddata db.json
fi
#python manage.py collectstatic --noinput

exec "$@"