FROM python:3.9-slim

WORKDIR /app

COPY main_cli.py /app/
COPY main_env.py /app/
COPY src /app/src
COPY requirements.txt /app/

RUN pip install -r requirements.txt
RUN apt-get update
RUN apt-get install -y dnsutils