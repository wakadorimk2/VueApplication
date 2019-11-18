from flask import Flask, jsonify
from flask_cors import CORS

from getFaves import getFaves

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/viewer', methods=['GET'])
def fav_images():
    return jsonify(getFaves())


if __name__ == '__main__':
    app.run()
