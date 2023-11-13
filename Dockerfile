FROM python:3.11-slim-buster

WORKDIR /src

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./app /src/
COPY ./requirements /requirements
COPY ./script /script

EXPOSE 8000

RUN apt update && apt upgrade -y build-essential libpq-dev
RUN pip install -r /requirements/base.txt