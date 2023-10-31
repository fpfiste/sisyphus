#!/bin/bash


timestamp=$(date +%s)
PGPASSWORD="$POSTGRES_PASSWORD" pg_dump -h $SQL_HOST -p $SQL_PORT -U $POSTGRES_USER $POSTGRES_DB > /backup/$timestamp.dump

