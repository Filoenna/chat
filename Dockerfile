FROM python:3.9.1

RUN mkdir /app

COPY ./app/server.py /app/server.py

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 8888

CMD [ "python", "server.py"]
