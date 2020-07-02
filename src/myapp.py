#!/usr/bin/env python
from flask import Flask, request


import os
myhost = os.uname()[1]


app = Flask(__name__)


@app.route("/")
def index():
    return myhost


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
