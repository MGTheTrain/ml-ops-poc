FROM python:3.9-slim

WORKDIR /app

COPY main.py /app/
COPY src /app/src
COPY requirements.txt /app/

RUN pip install -r requirements.txt