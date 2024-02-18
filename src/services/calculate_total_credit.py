from fetch_data_from_file import FileData

def calculate(enrolled_courses, courses):
  
  total_credit = {}
  ignore_grades = ["P", "F", "W"]
  
  for enrolled_course in enrolled_courses:
    for course in courses:
      if course["course_id"] == enrolled_course["course_id"] and enrolled_course["student_grade"] not in ignore_grades:
        if course["course_category"] not in total_credit:
          total_credit[course["course_category"]] = course["course_credit"]
        else:
          total_credit[course["course_category"]] += course["course_credit"]
          
        if course["course_faculty"] not in total_credit:
          total_credit[course["course_faculty"]] = course["course_credit"]
        else:
          total_credit[course["course_faculty"]] += course["course_credit"]
          
  return total_credit


f = FileData()
courses = f.fetch()

enrolled_courses = [
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
]

total_credit = calculate(enrolled_courses, courses)  

print(total_credit)
print(sum(total_credit.values()))
