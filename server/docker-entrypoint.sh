#!/bin/bash

if [ "$1" = 'api' ]; then
    echo "Running api services"
    flask run
fi