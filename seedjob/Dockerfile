FROM python:3.8-alpine

ENV PATH="/scripts:${PATH}"

COPY requirements.txt /requirements.txt

RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers
RUN apk add --update mysql-client
RUN apk add --update mariadb-dev
RUN pip3 install -r /requirements.txt

RUN apk del .tmp

RUN mkdir /scripts

COPY ./products.csv /products.csv
COPY ./users.csv /users.csv

WORKDIR /scripts

COPY ./load_data.py /scripts/load_data.py

CMD ["python3 /scripts/load_data.py"]
