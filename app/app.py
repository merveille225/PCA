from flask import Flask
import redis
import os
import time

app = Flask(__name__)
redis_client = redis.Redis(host="redis", port=6379, decode_responses=True)

@app.route("/")
def index():
    # simple counter stored in redis
    try:
        redis_client.incr("counter")
        count = redis_client.get("counter") or "0"
    except Exception as e:
        count = "redis-error"
    name = os.getenv("APP_NAME", "Web")
    return f"<h1>Hello from {name}</h1><p>Visits: {count}</p><p>Time: {time.ctime()}</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

