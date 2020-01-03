#!/bin/env python

import os
import signal
import redis
import pickle
import json
from flask import Flask
from buzz import generator

app = Flask(__name__)

signal.signal(signal.SIGINT, lambda s, f: os._exit(0))

@app.before_first_request
def init_redis():
    with open('/opt/webapp/data/data.json') as json_file:
        r = redis.from_url(os.environ.get("REDIS_URL"))
        data = json.load(json_file)
        for key in data.keys():
            r.set(key, pickle.dumps(data[key]))

@app.route("/")
def generate_buzz():
    page = '<html><body><h1>'
    page += generator.generate_buzz()
    page += '</h1></body></html>'
    return page

@app.route("/redis")
def generate_buzz_redis():
    r = redis.from_url(os.environ.get("REDIS_URL"))
    page = '<html><body><h1>'
    page += generator.generate_buzz_redis(r)
    page += '</h1><footer><p>Powered by Redis</p></footer></body></html>'
    return page

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.getenv('PORT')) # port 5000 is the default
