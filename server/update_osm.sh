#!/bin/bash

cd /osm-data 
if test -f "/osm-data/norway-latest.osm.pbf"; then
    echo "file exist"
else
    wget https://download.geofabrik.de/europe/norway-latest.osm.pbf
    export PGPASSWORD=admin
    osm2pgsql -d postgres -C 4096 -U postgres -W -H db -P 5432 /osm-data/norway-latest.osm.pbf
fi