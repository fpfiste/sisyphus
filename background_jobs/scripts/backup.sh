#!/bin/bash

find /backup/ -mindepth 1 -mtime +90 -delete

timestamp=$(date +%Y%m%d_%H%M%S)
PGPASSWORD="$POSTGRES_PASSWORD" pg_dump -h $SQL_HOST -p $SQL_PORT -U $POSTGRES_USER $POSTGRES_DB > /backup/$timestamp.dump

