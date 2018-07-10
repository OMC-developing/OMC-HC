FROM alpine
MAINTAINER Max Pisarenko <makzzz1986@gmail.com>
MAINTAINER Artem Udovichenko <aptem-1986@yandex.ru>

# install python 2.7, PIP, docker lib, Flask
RUN apk add python 
RUN apk add py-pip
RUN pip install docker flask flask-sqlalchemy flask-restful flask-jsonpify
RUN mkdir -p /home/flask/

COPY ./flask_engine/ /home/flask/
WORKDIR /home/flask

ENTRYPOINT ["python"]
CMD ["app.py"]


