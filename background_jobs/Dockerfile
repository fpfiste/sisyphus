# Pulling Ubuntu image
FROM ubuntu:20.04

# Updating packages and installing cron
RUN apt-get update && apt-get install cron -y 

COPY ./requirements.txt /

RUN pip install -r /requirements.txt

# Adding crontab to the appropriate location
ADD cronjobs /etc/cron.d/cronjobs

# Giving permission to crontab file
RUN chmod 0644 /etc/cron.d/cronjobs

# Running crontab
RUN crontab /etc/cron.d/cronjobs

# Creating entry point for cron 
ENTRYPOINT ["cron", "-f"]