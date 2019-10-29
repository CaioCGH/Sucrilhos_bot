FROM python:3.7-alpine
WORKDIR /usr/src

COPY requirements.txt requirements.txt
RUN apk add --update --no-cache \
      sqlite \
      curl \
      less \
      && rm -rf /var/cache/apk/*

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt