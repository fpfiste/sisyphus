#!/bin/bash

timestamp=$(date +%s)
pg_dump -h localhost -p 5433 -U hello_django sisyphus > /backup/$timestamp.dump

