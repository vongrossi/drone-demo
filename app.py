from flask import Flask
import redis
import os
import socket

# Connect to Redis
r = redis.from_url(os.getenv("REDIS_URL", "redis://redis"), db=0, socket_connect_timeout=2, socket_timeout=2)

app = Flask(__name__)

@app.route("/")
def hello():
    try:
        visits = r.incr("counter")
    except redis.RedisError as e:
        visits = "<i>cannot connect to Redis, counter disabled</i>"

    html = "<h3>Hello {name}!</h3>"            "<b>Hostname:</b> {hostname}<br/>"            "<b>Visits:</b> {visits}"
    return html.format(name="Estabilis", hostname=socket.gethostname(), visits=visits)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.getenv("PORT", "4000")))

