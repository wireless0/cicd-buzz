#!/bin/sh -x

mongod --fork --syslog
mongoimport --db=buzz --collection=generator --file=/src/data.json --jsonArray
python3 /src/app.py
