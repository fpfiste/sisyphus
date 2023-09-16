#!/bin/sh

if [ "$DATABASE" = "sisyphus" ]

then
    echo "Waiting for sisyphus..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python manage.py migrate

gunicorn main.wsgi:application --bind 0.0.0.0:8000


