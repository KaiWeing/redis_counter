FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7

# for testing
# RUN apk --update add curl redis
COPY ./app /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

ENV REDIS_HOST redis
ENV REDIS_PORT 6379

