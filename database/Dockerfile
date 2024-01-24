FROM postgres:13.0-alpine
COPY seed_data /docker-entrypoint-initdb.d/
COPY ./scripts/1_init.sql /docker-entrypoint-initdb.d/
COPY scripts/2_extensions.sql /docker-entrypoint-initdb.d/
COPY scripts/3_seed.sql /docker-entrypoint-initdb.d/
COPY scripts/4_update.sql /docker-entrypoint-initdb.d/
RUN mkdir -p /data


