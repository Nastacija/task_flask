from flask import Flask, render_template, jsonify
import random
import json

app = Flask(__name__)

with open('quotes.json') as json_file:
        data = json.load(json_file) 

@app.route("/")
def fnc():
    return render_template('quotes.html', quote = data[str(random.randrange(1, 4))])

@app.route('/api', methods=['GET', 'POST'])
def api():
    return jsonify({'quote': data[str(random.randrange(1, 4))]})

if __name__ == "__main__":
    app.run(debug=True)