#!/usr/bin/python3
"""
This is a simple Flask web application that listens on 0.0.0.0, port 5000.
It defines a single route '/' that displays "Hello HBNB!" when accessed.
"""

from flask import Flask, render_template
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

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
   """
   display “C ” followed by the value of the text variable.
   """
   return 'C ' + text.replace('_', ' ')

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """
    display "Python" folowed by the value of the next variable.
    """
    return 'Python ' + text.replace('_', ' ')

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    display "n"
    """
    return f"{n} is a number"
@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    display a HTML page only if n is an integer:
    H1 tag: “Number: n” inside the tag BODY
    """
    return render_template('5-number.html', n=n)

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000)
