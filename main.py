import atexit

from flask import Flask, render_template, request, jsonify
from flask_redis import FlaskRedis
from backend.wordle_solver import get_guesses

app = Flask(__name__)
app.config['REDIS_URL'] = 'redis://localhost:6379/0'
redis_client = FlaskRedis(app)

@atexit.register
def cleanup():
    redis_client.flushall()
    print("Redis flushed")
    print("App closed")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=['POST'])
def submit():
    print("Submit request received\n")
    data = request.get_json()
    add_data_to_redis(data)
    grn = [b.decode('utf-8') for b in redis_client.lrange('greens', 0, -1)]
    yel = [b.decode('utf-8') for b in redis_client.lrange('yellows', 0, -1)]
    gry = [b.decode('utf-8') for b in redis_client.lrange('grays', 0, -1)]
    print("Data retrieved from redis")
    print(f"Greens: {grn}\nYellows: {yel}\nGrays: {gry}\n")
    guesses = get_guesses(grn, yel, gry)
    print(f"Guesses: {guesses}")
    return jsonify({'guesses': guesses})

def add_data_to_redis(data):
    grn = data.get('greens')
    yel = data.get('yellows')
    gry = data.get('grays')

    print("Adding data to redis")
    print(f"greens: {grn}\nyellows: {yel}\ngrays: {gry}\n")

    if len(grn) > 0:
        redis_client.rpush('greens', *grn)
    if len(yel) > 0:
        redis_client.rpush('yellows', *yel)
    if len(gry) > 0:
        redis_client.rpush('grays', *gry)

    print("Redis pushed\n")

if __name__ == "__main__":
    app.run()