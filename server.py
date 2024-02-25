#!/usr/bin/env python

import os
from flask import Flask, request, render_template, jsonify
# from flask_api import status
from script import get_student_data
import sys
sys.path.append("src/services")
from check_graduation import check_graduation
from calculate_total_credit import calculate
from data_source_file import DataSourceFile

import insert

# Support for gomix's 'front-end' and 'back-end' UI.
app = Flask(__name__, static_folder='public', template_folder='views')

# Set the app secret key from the secret environment variables.
app.secret = os.environ.get('SECRET')

def allowed_file(filename):
  ALLOWED_EXTENSIONS = { 'pdf' }
  print(filename)
  return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def homepage():
  """Displays the homepage."""
  return render_template('index.html')

@app.route('/api/upload', methods=['POST'])
def upload():
  
  if request.method == 'POST':   
    
    # Check file type is PDF
    if 'file' not in request.files:
      return "No file uploaded", 400

    f = request.files['file'] 

    if not allowed_file(f.filename):
      return "File type not allowed only support pdf", 400

    student_data = get_student_data(f)
    student_data.update({
      "total_credit_per_category": calculate(student_data["enrolled_courses"], DataSourceFile())
    })

    return jsonify(check_graduation(student_data))
  
if __name__ == '__main__':
  insert.sync(DataSourceFile().fetch())
  
  app.run(debug = True)