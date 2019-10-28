FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN mkdir /twilio
WORKDIR /twilio

COPY setup.py .
COPY requirements.txt .
COPY README.md .
COPY twilio ./twilio

RUN pip install .
