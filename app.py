from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from db import db
from ma import ma

app = Flask(__name__)
api = Api(app, prefix="/api/v1")
CORS(app, resources=r"/api/*", allow_headers="Content-Type")


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    db.init_app(app)
    ma.init_app(app)
    app.run(host="0.0.0.0", port=5000, debug=True)
