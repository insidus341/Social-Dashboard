from flask import json, render_template, Flask, request
from modules.update_counters import get_counter

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/update', methods=['GET'])
def update():
    return get_counter()


if __name__ == '__main__':
    app.run('localhost', 5000, debug=False)