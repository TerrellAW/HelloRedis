from flask import Flask
import redis

app = Flask(__name__)

@app.route('/')
def hello():
    r = redis.Redis(host='redis', port=6379, decode_responses=True)
    name = r.get('name')
    if name:
        return f"Hello {name}"

    return "Hello Guest"

if __name__ == '__main__':
    app.run("0.0.0.0", port=5000)
