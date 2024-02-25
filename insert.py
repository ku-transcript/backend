import db

def sync(data):
  conn = db.get_db_connection()
  cur = conn.cursor()
    
  # Insert data into the table
  for course in data:
      cur.execute("INSERT INTO courses (course_id, course_name, course_credit, course_category, course_faculty) VALUES (?, ?, ?, ?, ?)", 
                  (course['course_id'], course['course_name'], course['course_credit'], course['course_category'], course.get('course_faculty', None)))

  conn.commit()
  conn.close()
  print("Inserted courses to the database.")
  
  