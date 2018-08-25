# coding: utf-8
from flask import Flask
from redis import Redis, RedisError
import os
import socket

# Connect to Redis
redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)

app = Flask(__name__)
# test
# test 1
@app.route("/")
def hello():
    try:
        visits = redis.incr("counter")
    except RedisError:
        visits = "<i>cannot connect to Redis, counter disabled</i>"

    html = "<h1>Test fix's</h1><h2>This server deployment from auto-build out docker</h2><br><h3>test autodeploy</h3>"
    return html


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
