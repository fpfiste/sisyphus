#!/bin/sh


echo "Waiting for sisyphus..."

while ! nc -z $SQL_HOST $SQL_PORT; do
  sleep 0.1
done

echo "PostgreSQL started"



python manage.py runserver 0.0.0.0:8002


