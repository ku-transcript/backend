#!/usr/bin/env python

import os
from flask import Flask, request, render_template, jsonify
from script import get_student_data
import sys
sys.path.append("src/services")
from check_graduation import check_graduation
from calculate_total_credit import calculate
from data_source_file import DataSourceFile

# Support for gomix's 'front-end' and 'back-end' UI.
app = Flask(__name__, static_folder='public', template_folder='views')

# Set the app secret key from the secret environment variables.
app.secret = os.environ.get('SECRET')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def homepage():
    """Displays the homepage."""
    return render_template('index.html')

@app.route('/api/upload', methods=['POST'])
def upload():
  ALLOWED_EXTENSION = { '.pdf' }
  
  if request.method == 'POST':   
    
        # TODO: check file type is PDF
        
        if 'file' not in request.files:
          return
        
        f = request.files['file'] 
        
        if f and allowed_file(f)
        
        student_data = get_student_data(f)
        student_data.update({
          "total_credit_per_category": calculate(student_data["enrolled_courses"], DataSourceFile())
        })
        
        return jsonify(check_graduation(student_data))
  
if __name__ == '__main__':
    app.run(debug = True)