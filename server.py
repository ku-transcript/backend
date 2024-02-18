#!/usr/bin/env python

import os
from flask import Flask, request, render_template, jsonify
from script import get_student_data
import sys
sys.path.append("src/services")
from check_graduation import check_graduation

# Support for gomix's 'front-end' and 'back-end' UI.
app = Flask(__name__, static_folder='public', template_folder='views')

# Set the app secret key from the secret environment variables.
app.secret = os.environ.get('SECRET')

@app.route('/')
def homepage():
    """Displays the homepage."""
    return render_template('index.html')

@app.route('/api/upload', methods=['POST'])
def upload():
  if request.method == 'POST':   
    
        # TODO: check file type is PDF
        f = request.files['file'] 
        
        student_data = get_student_data(f)
        
        return jsonify(check_graduation(student_data))
  
if __name__ == '__main__':
    app.run(debug = True)