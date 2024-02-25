import sqlite3

import json

from os import listdir
from os.path import isfile, join

# Create a connection to the database
conn = sqlite3.connect('courses.db')

# path contain files of courses
path = "./data"
print(listdir(path))
files = [f for f in listdir(path) if isfile(join(path, f))]
data = []

for file in files:
  data.extend(json.load(open(join(path, file))))
    
cur = conn.cursor()

print(data)

# Insert data into the table
for course in data:
    cur.execute("INSERT INTO courses (course_id, course_name, course_credit, course_category, course_faculty) VALUES (?, ?, ?, ?, ?)", 
                (course['course_id'], course['course_name'], course['course_credit'], course['course_category'], course.get('course_faculty', None)))
    

conn.commit()
print("Inserted courses to the database.")