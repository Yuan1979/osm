## osm

Simple API service demo to expose the data from OSM.

## Prerequisites

In order to run the commands described below, you need:
- Docker 
- osm2pgsql 
- Django

## Initial setup
```
./init_osm_db.sh
```
It will start a postpresql databse server with postgis extensions. For demo purpose, luxembourg data will be downloaded and injected into the database.

## Flask implementation
```
cd server
docker build -t osm-api .
docker run --rm --network=host osm-api
```
Then the number of nodes can be accessed by localhost/api/0.1/nodes.

## Django implementation
```
cd DjangoOsm
http://localhost:8000/nodes/
```
The all the nodes in the planet_osm_point table can be accessed by http://localhost:8000/nodes/.
