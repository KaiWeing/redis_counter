FROM docteurfraise/flask-python34

RUN apt-get -yqq update && apt-get -yqq install curl redis-tools

ENV REDIS_HOST redis
ENV REDIS_PORT 6379

