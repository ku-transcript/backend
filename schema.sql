CREATE TABLE IF NOT EXISTS courses (
    course_id CHAR(8) PRIMARY KEY, 
    course_name VARCHAR(255), 
    course_credit INT, 
    course_category VARCHAR(255), 
    course_faculty VARCHAR(255)
);
