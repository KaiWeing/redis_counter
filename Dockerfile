FROM docteurfraise/flask-python34

RUN apt-get -yqq update && apt-get -yqq install curl redis-cli

