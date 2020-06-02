from dotenv import load_dotenv
load_dotenv('config.env')


from flask import json, render_template, Flask, request
from modules.update_counters import get_counter
from modules.get_environmentals import app_ip, app_port


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/update', methods=['GET'])
def update():
    return get_counter()


if __name__ == '__main__':
    app.run(app_ip, app_port, debug=False)