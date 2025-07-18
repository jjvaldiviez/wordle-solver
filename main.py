from flask import Flask, render_template, request, jsonify

from backend.database.word_db import get_word_options

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=['POST'])
def submit():
    data = request.get_json()
    grn = data.get('greens')
    yel = data.get('yellows')
    gry = data.get('grays')
    options = get_word_options(grn, yel, gry)
    guesses = [v for v in options if len(v) == 5]
    print(guesses)
    return jsonify({'guesses': guesses})

if __name__ == "__main__":
    app.run()