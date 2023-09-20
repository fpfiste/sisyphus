FROM postgres:13.0-alpine
COPY seed_data /docker-entrypoint-initdb.d/
COPY init.sql /docker-entrypoint-initdb.d/