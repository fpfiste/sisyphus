FROM postgres:13.0-alpine
COPY seed_data /docker-entrypoint-initdb.d/
COPY ./scripts/1_init.sql /docker-entrypoint-initdb.d/
COPY ./scripts/2_seed.sql /docker-entrypoint-initdb.d/
