import sqlite3

def get_db_connection():
    conn = sqlite3.connect('courses.db')
    conn.row_factory = sqlite3.Row
    return conn
  
def sync(data):
    conn = get_db_connection()
    cur = conn.cursor()

    # Remove before sync
    cur.execute("DELETE FROM courses")

    # Insert courses to the database.
    for course in data:
      cur.execute("INSERT INTO courses (course_id, course_name, course_credit, course_category, course_faculty) VALUES (?, ?, ?, ?, ?)", 
                  (course['course_id'], course['course_name'], course['course_credit'], course['course_category'], course.get('course_faculty', None)))

    conn.commit()
    conn.close() 

    print("Courses Data insert successfully.")