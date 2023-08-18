#!/usr/bin/python3
"""a script that starts a Flask web application:
the web application must be listening on 0.0.0.0, port 5000
Routes: /: display “Hello HBNB!”
You must use the option strict_slashes=False in your route definition
"""
from flask import Flask


app = Flask(__name__)
app.debug = False


@app.route("/airbnb-onepage/", strict_slashes=False)
def hello():
    """Displays 'Hello HBNB!'"""
    return ("Hello HBNB!")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
