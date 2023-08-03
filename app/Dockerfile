


# pull official base image
FROM python:3.9.6-alpine

# set work directory
RUN mkdir /home/app
WORKDIR /home/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev





# copy project
COPY . .

# install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


RUN chmod +x entrypoint.sh

CMD ['sh', './entrypoint.sh']