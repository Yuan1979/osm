FROM python:3.7

#ENV FLASK_APP app.py
#ENV FLASK_RUN_PORT 80
#ENV FLASK_RUN_HOST 0.0.0.0

RUN apt-get update && apt-get -y install \
    wget \
    osm2pgsql

RUN mkdir /osm-data

RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/

EXPOSE 80

ENTRYPOINT [ "./update_osm.sh" ]

