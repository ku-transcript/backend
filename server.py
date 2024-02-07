#!/usr/bin/env python

import os
from flask import Flask, request, render_template, jsonify
import test
from script import getTextFromPDF

# Support for gomix's 'front-end' and 'back-end' UI.
app = Flask(__name__, static_folder='public', template_folder='views')

# Set the app secret key from the secret environment variables.
app.secret = os.environ.get('SECRET')

# Dream database. Store dreams in memory for now. 
DREAMS = ['Python. Python, everywhere.']

@app.route('/')
def homepage():
    """Displays the homepage."""
    return render_template('index.html')
  
# @app.route('/dreams', methods=['GET', 'POST'])
# def helloworld():

@app.route('/api/upload', methods=['POST'])
def upload():
  if request.method == 'POST':   
        f = request.files['file'] 
        # f.save(f.filename)   
        print(getTextFromPDF(f))
        
        return "file uploaded"
  


if __name__ == '__main__':
    app.run(debug = True)