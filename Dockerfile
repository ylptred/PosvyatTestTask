FROM python:latest


ADD server.py /server/
ADD index.html /server/

RUN pip install --upgrade pip && \
    pip install bs4

RUN pip install requests

RUN pip install lxml




WORKDIR /server/