FROM python:3.10-alpine

ENV PYTHONUNBUFFERED 1
ENV PIP_NO_CACHE_DIR 1

RUN mkdir /igsmanager
WORKDIR /igsmanager
COPY requirements.txt /igsmanager/
RUN pip install -r requirements.txt
COPY . /igsmanager/