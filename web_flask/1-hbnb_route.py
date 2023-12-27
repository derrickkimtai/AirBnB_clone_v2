#!/usr/bin/python3
"""
This is a simple Flask web application that listens on 0.0.0.0, port 5000.
It defines a single route '/' that displays "Hello HBNB!" when accessed.
"""

from flask import Flask
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
   """
   This function handles requests to the root URL of the server.
   It returns the string 'Hello HBNB!'.
   """
   return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def bnb():
   """
   This function handles requests to the root URL of the server.
   It returns the string HBNB!'.
   """
   return 'HBNB'

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000)

