from flask import Flask, jsonify
from create_drink import *

app = Flask(__name__)



@app.route('/random', methods=['GET'])
def get_random_drink():

    random_drink = {
        "drink": make_random_drink()
        }

    return jsonify(random_drink)

if __name__ == "__main__":
    app.run(host='localhost', port=8088, debug=True )