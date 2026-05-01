from flask import Flask
import redis
import os

app = Flask(__name__)


host = os.getenv("REDIS_HOST", "redis")
port = int(os.getenv("REDIS_PORT", 6379))

r = redis.Redis(host=host, port=port)
@app.route("/")
def hello():
    return "Hello to CoderCo Containers Challenge"

@app.route("/count")
def visitsCount():
    count = r.incr('visits')
    return f'This page has been visited {count} times.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)