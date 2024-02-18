import re

class CS60Validator:
  
  required_credit = {
    'วิชาแกน': 16, 
    'วิชาเฉพาะบังคับ': 55, 
    'วิชาเฉพาะเลือก': 21, 
    'ภาษากับการสื่อสาร': 13, 
    'พลเมืองไทยและพลเมืองโลก': 3, 
    'ศาสตร์แห่งผู้ประกอบการ': 3, 
    'สุนทรียศาสตร์': 3, 
    'อยู่ดีมีสุข': 3,
    'คณะวิทยาศาสตร์': 5,
  }
  
  def validate(self, student_data, total_credit):
        
    # check credit
    course_categories = self.required_credit.keys()
    
    for course_category in course_categories:
      if total_credit[course_category] < self.required_credit[course_category]:
        return False
      
    # check required course (e.g. P.E, Eng)
    enrolled_courses = student_data["enrolled_courses"]
    
    sport = 0
    eng = 0
    thai = 0
    knowledge_of_the_land = 0
    digital = 0
    science = 0
    
    for enrolled_course in enrolled_courses:
      course_id = enrolled_course["course_id"]
      
      # sport
      if re.search("01175\d{3}", course_id):
        sport += 1
            
      # eng
      if re.search("01355\d{3}", course_id):
        eng += 1
      
      # thai
      if re.search("01361101|01361102|01361103|01999021|01999022|02701011", course_id):
        thai += 1
      
      # knowledge of the land
      if re.search("01999111", course_id):
        knowledge_of_the_land += 1
      
      # digital
      if re.search("01418131|01420245|01420246", course_id):
        digital += 1
            
    if sport < 1 or eng < 3 or thai < 1 or knowledge_of_the_land < 1 or digital < 1:
      return False
      
    # check grade
    if student_data["student_cum_gpa"] < 2:
      return False
      
    return True
  
  
# sample
total_credit = {'วิชาแกน': 16, 'วิชาเฉพาะบังคับ': 35, 'วิชาเฉพาะเลือก': 18, 'ภาษากับการสื่อสาร': 7, 'พลเมืองไทยและพลเมืองโลก': 3, 'ศาสตร์แห่งผู้ประกอบการ': 3, 'สุนทรียศาสตร์': 3, 'อยู่ดีมีสุข': 9}

student_data = {
    "enrolled_courses": [
        {
            "course_credit": "3",
            "course_id": "01355101",
            "course_name": "English for Everyday Life",
            "student_grade": "P"
        },
        {
            "course_credit": "3",
            "course_id": "01355102",
            "course_name": "English for University Life",
            "student_grade": "P"
        },
        {
            "course_credit": "3",
            "course_id": "01417111",
            "course_name": "Calculus I",
            "student_grade": "B"
        },
        {
            "course_credit": "3",
            "course_id": "01418112",
            "course_name": "Fundamental Programming Concepts",
            "student_grade": "B+"
        },
        {
            "course_credit": "2",
            "course_id": "01418114",
            "course_name": "Introduction to Computer Science",
            "student_grade": "A"
        },
        {
            "course_credit": "3",
            "course_id": "01418131",
            "course_name": "Digital Computer Logic",
            "student_grade": "A"
        },
        {
            "course_credit": "3",
            "course_id": "01999021",
            "course_name": "Thai Language for Communication",
            "student_grade": "A"
        },
        {
            "course_credit": "2",
            "course_id": "01999111",
            "course_name": "Knowledge of the Land",
            "student_grade": "A"
        },
        {
            "course_credit": "3",
            "course_id": "01177141",
            "course_name": "Knowledge Acquisition",
            "student_grade": "A"
        },
        {
            "course_credit": "3",
            "course_id": "01255101",
            "course_name": "Man and Sea",
            "student_grade": "A"
        },
        {
            "course_credit": "3",
            "course_id": "01355103",
            "course_name": "English for Job Opportunities",
            "student_grade": "B"
        },
        {
            "course_credit": "1",
            "course_id": "01371111",
            "course_name": "Information Media for Learning",
            "student_grade": "A"
        },
        {
            "course_credit": "3",
            "course_id": "01417112",
            "course_name": "Calculus II",
            "student_grade": "W"
        },
        {
            "course_credit": "3",
            "course_id": "01418113",
            "course_name": "Computer Programming",
            "student_grade": "A"
        },
        {
            "course_credit": "4",
            "course_id": "01418132",
            "course_name": "Fundamentals of Computing",
            "student_grade": "B+"
        },
        {
            "course_credit": "1",
            "course_id": "02999144",
            "course_name": "Life Skills For Undergraduate Student",
            "student_grade": "A"
        },
        {
            "course_credit": "3",
            "course_id": "01417112",
            "course_name": "Calculus II",
            "student_grade": "A"
        },
        {
            "course_credit": "3",
            "course_id": "01999012",
            "course_name": "Health for Life",
            "student_grade": "A"
        },
        {
            "course_credit": "1",
            "course_id": "01175127",
            "course_name": "Hockey for Health",
            "student_grade": "A"
        },
        {
            "course_credit": "3",
            "course_id": "01417322",
            "course_name": "ฺBasic Linear Algebra",
            "student_grade": "B+"
        },
        {
            "course_credit": "3",
            "course_id": "01418211",
            "course_name": "Software Construction",
            "student_grade": "A"
        },
        {
            "course_credit": "3",
            "course_id": "01418231",
            "course_name": "Data Structures",
            "student_grade": "B+"
        },
        {
            "course_credit": "2",
            "course_id": "01421201",
            "course_name": "Radiation, Life and Environment",
            "student_grade": "A"
        },
        {
            "course_credit": "3",
            "course_id": "01422111",
            "course_name": "Principles of Statistics",
            "student_grade": "B+"
        },
        {
            "course_credit": "3",
            "course_id": "01459101",
            "course_name": "Psychology for Modern Life",
            "student_grade": "W"
        },
        {
            "course_credit": "3",
            "course_id": "01418221",
            "course_name": "Fundamentals of Database Systems",
            "student_grade": "B"
        },
        {
            "course_credit": "3",
            "course_id": "01418232",
            "course_name": "Algorithm Design and Analysis",
            "student_grade": "B+"
        },
        {
            "course_credit": "4",
            "course_id": "01418233",
            "course_name": "Assembly Language and Computer Architecture",
            "student_grade": "A"
        },
        {
            "course_credit": "3",
            "course_id": "01418323",
            "course_name": "Introduction to Data Science",
            "student_grade": "B"
        },
        {
            "course_credit": "3",
            "course_id": "01418496",
            "course_name": "Selected Topic in Computer Science",
            "student_grade": "B"
        },
        {
            "course_credit": "3",
            "course_id": "01999033",
            "course_name": "Arts of Living",
            "student_grade": "A"
        },
        {
            "course_credit": "3",
            "course_id": "01418235",
            "course_name": "Unix Operating System and Shell Programming",
            "student_grade": "A"
        },
        {
            "course_credit": "3",
            "course_id": "01418321",
            "course_name": "System Analysis and Design",
            "student_grade": "B+"
        },
        {
            "course_credit": "4",
            "course_id": "01418331",
            "course_name": "Operating Systems",
            "student_grade": "A"
        },
        {
            "course_credit": "3",
            "course_id": "01418341",
            "course_name": "Intellectual Properties and Professional Ethics",
            "student_grade": "C+"
        },
        {
            "course_credit": "3",
            "course_id": "01418442",
            "course_name": "Web Technology and Web Services",
            "student_grade": "B+"
        },
        {
            "course_credit": "3",
            "course_id": "01418471",
            "course_name": "Introduction to Software Engineering",
            "student_grade": "A"
        },
        {
            "course_credit": "1",
            "course_id": "01418497",
            "course_name": "Seminar",
            "student_grade": "C+"
        }
    ],
    "student_cum_gpa": 3.64,
    "student_en_name": "NAPATSORN LAOPITAKKUL",
    "student_en_title": "Miss",
    "student_faculty": "Faculty Of Science",
    "student_id": "6410406711",
    "student_major": "Computer Science",
    "student_th_name": "นภัสสร เลาพิทักษ์กูล",
    "student_th_title": "นางสาว"
}

validator = CS60Validator()

print(validator.validate(None, total_credit))