FROM python:3.10.9

ENV PYTHONUNBUFFERED 1

RUN mkdir /twilio
WORKDIR /twilio

COPY setup.py .
COPY requirements.txt .
COPY README.md .
COPY twilio ./twilio
COPY tests ./tests

RUN pip install .
RUN pip install -r tests/requirements.txt
