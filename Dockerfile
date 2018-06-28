FROM python:3.5

MAINTAINER Roman Blinov

RUN mkdir /kabinet
COPY . /kabinet
COPY .env.deploy /kabinet/.env
WORKDIR /kabinet

RUN pip install -r requirements.txt
RUN pip install uwsgi
RUN python ./manage.py clean_pyc

CMD uwsgi --http-socket 0.0.0.0:8000 --wsgi-file /kabinet/kabinet/wsgi.py