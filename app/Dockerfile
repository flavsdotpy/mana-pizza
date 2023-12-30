FROM python:3.10-slim-bullseye

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=1.7.1

RUN apt-get update \
    && apt-get -y install \
      gcc

RUN pip install "poetry==$POETRY_VERSION"

RUN mkdir -p /app
ADD app /app

RUN mkdir -p /lib
add library /lib

WORKDIR /lib
RUN poetry config virtualenvs.create false && poetry install

WORKDIR /app
RUN poetry config virtualenvs.create false && poetry install --no-root

EXPOSE 5000
CMD ["uwsgi", "--ini", "/app/wsgi.ini"]
