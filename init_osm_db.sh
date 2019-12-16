#!/bin/bash

set +e

echo "start postgis server...."
docker run --rm --network=host -e POSTGRES_PASSWORD=admin -d -h 127.0.0.1 -p 5432:5432 mdillon/postgis

echo "downloading osm data from geofabrik..."
wget https://download.geofabrik.de/europe/luxembourg-latest.osm.pbf

echo "sending data to postgis server"
export PGPASSWORD=admin
osm2pgsql -d postgres -C 4096 -U postgres -H 127.0.0.1 -P 5432 luxembourg-latest.osm.pbf

set -e
