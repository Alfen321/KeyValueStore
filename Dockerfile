FROM ubuntu:18.04

RUN apt install -y python3-pip &&\
    apt clean && \
    mkdir /app

COPY . /app

RUN pip3 install -r /app/requirements

EXPOSE 5000

WORKDIR /app

CMD python3 main.py