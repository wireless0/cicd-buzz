import os
import signal
from flask import Flask
from pymongo import MongoClient
from buzz import generator

app = Flask(__name__)

signal.signal(signal.SIGINT, lambda s, f: os._exit(0))

@app.route("/")
def generate_buzz():
    page = '<html><body><h1>'
    page += generator.generate_buzz()
    page += '</h1></body></html>'
    return page

@app.route("/mongo")
def generate_buzz_mongo():
    collection = MongoClient('mongodb://127.0.0.1:27017/')['buzz']['generator']
    page = '<html><body><h1>'
    page += generator.generate_buzz_mongo(collection)
    page += '</h1><footer><p>Powered by MongoDB</p></footer></body></html>'
    return page

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.getenv('PORT')) # port 5000 is the default
