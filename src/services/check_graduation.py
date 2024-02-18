from validate_data import validate
from calculate_total_credit import calculate
from data_source_file import DataSourceFile
# Quickly import file from another folder (NOT GOOD!)
import sys
sys.path.append("src/validator")
from cs60_validator import CS60Validator

def check_graduation(student_data):
  student_id = student_data["student_id"]
  years = int(student_id[0:2])
  
  total_credit = calculate(student_data["enrolled_courses"], DataSourceFile())
  
  result = None
  
  # (FUTURE) Add more if-else for different major and years
  if student_data["student_major"] == "Computer Science" and years >= 60 and years < 65:
    result = validate(student_data, total_credit, CS60Validator())
  
  # Currently except only CS Major (TODO: throw error)
  
  student_data.update({
    "is_graduate": result,
    "total_credit_per_category": total_credit
  })
  
  return student_data
  
  
# Test
student_data = {
    "enrolled_courses": [
        {
            "course_credit": 3,
            "course_id": "01355101",
            "course_name": "English for Everyday Life",
            "student_grade": "P"
        },
        {
            "course_credit": 3,
            "course_id": "01355102",
            "course_name": "English for University Life",
            "student_grade": "P"
        },
        {
            "course_credit": 3,
            "course_id": "01387101",
            "course_name": "The Art of Living with Others",
            "student_grade": "A"
        },
        {
            "course_credit": 3,
            "course_id": "01417111",
            "course_name": "Calculus I",
            "student_grade": "A"
        },
        {
            "course_credit": 3,
            "course_id": "01418112",
            "course_name": "Fundamental Programming Concepts",
            "student_grade": "A"
        },
        {
            "course_credit": 2,
            "course_id": "01418114",
            "course_name": "Introduction to Computer Science",
            "student_grade": "B+"
        },
        {
            "course_credit": 3,
            "course_id": "01418131",
            "course_name": "Digital Computer Logic",
            "student_grade": "A"
        },
        {
            "course_credit": 3,
            "course_id": "01999021",
            "course_name": "Thai Language for Communication",
            "student_grade": "A"
        },
        {
            "course_credit": 2,
            "course_id": "01999111",
            "course_name": "Knowledge of the Land",
            "student_grade": "A"
        },
        {
            "course_credit": 3,
            "course_id": "01177141",
            "course_name": "Knowledge Acquisition",
            "student_grade": "A"
        },
        {
            "course_credit": 3,
            "course_id": "01255101",
            "course_name": "Man and Sea",
            "student_grade": "A"
        },
        {
            "course_credit": 3,
            "course_id": "01355103",
            "course_name": "English for Job Opportunities",
            "student_grade": "B+"
        },
        {
            "course_credit": 3,
            "course_id": "01417112",
            "course_name": "Calculus II",
            "student_grade": "A"
        },
        {
            "course_credit": 3,
            "course_id": "01418113",
            "course_name": "Computer Programming",
            "student_grade": "A"
        },
        {
            "course_credit": 4,
            "course_id": "01418132",
            "course_name": "Fundamentals of Computing",
            "student_grade": "A"
        },
        {
            "course_credit": 1,
            "course_id": "02999144",
            "course_name": "Life Skills For Undergraduate Student",
            "student_grade": "A"
        },
        {
            "course_credit": 1,
            "course_id": "01175143",
            "course_name": "Social Dance for Health",
            "student_grade": "A"
        },
        {
            "course_credit": 1,
            "course_id": "01371111",
            "course_name": "Information Media for Learning",
            "student_grade": "A"
        },
        {
            "course_credit": 3,
            "course_id": "01417322",
            "course_name": "ฺBasic Linear Algebra",
            "student_grade": "A"
        },
        {
            "course_credit": 3,
            "course_id": "01418211",
            "course_name": "Software Construction",
            "student_grade": "A"
        },
        {
            "course_credit": 3,
            "course_id": "01418231",
            "course_name": "Data Structures",
            "student_grade": "A"
        },
        {
            "course_credit": 2,
            "course_id": "01421201",
            "course_name": "Radiation, Life and Environment",
            "student_grade": "A"
        },
        {
            "course_credit": 3,
            "course_id": "01422111",
            "course_name": "Principles of Statistics",
            "student_grade": "A"
        },
        {
            "course_credit": 3,
            "course_id": "01999011",
            "course_name": "Food for Mankind",
            "student_grade": "B+"
        },
        {
            "course_credit": 3,
            "course_id": "01387102",
            "course_name": "Philosophy for New Life",
            "student_grade": "A"
        },
        {
            "course_credit": 3,
            "course_id": "01401201",
            "course_name": "Plants for Value of Life Creation",
            "student_grade": "A"
        },
        {
            "course_credit": 3,
            "course_id": "01418221",
            "course_name": "Fundamentals of Database Systems",
            "student_grade": "A"
        },
        {
            "course_credit": 3,
            "course_id": "01418232",
            "course_name": "Algorithm Design and Analysis",
            "student_grade": "A"
        },
        {
            "course_credit": 4,
            "course_id": "01418233",
            "course_name": "Assembly Language and Computer Architecture",
            "student_grade": "A"
        },
        {
            "course_credit": 3,
            "course_id": "01418241",
            "course_name": "Financial and Bangking Information Technology",
            "student_grade": "A"
        },
        {
            "course_credit": 3,
            "course_id": "01418475",
            "course_name": "Software Testing and Verification",
            "student_grade": "A"
        },
        {
            "course_credit": 3,
            "course_id": "01418321",
            "course_name": "System Analysis and Design",
            "student_grade": "A"
        },
        {
            "course_credit": 4,
            "course_id": "01418331",
            "course_name": "Operating Systems",
            "student_grade": "A"
        },
        {
            "course_credit": 3,
            "course_id": "01418341",
            "course_name": "Intellectual Properties and Professional Ethics",
            "student_grade": "A"
        },
        {
            "course_credit": 3,
            "course_id": "01418442",
            "course_name": "Web Technology and Web Services",
            "student_grade": "A"
        },
        {
            "course_credit": 3,
            "course_id": "01418471",
            "course_name": "Introduction to Software Engineering",
            "student_grade": "A"
        },
        {
            "course_credit": 1,
            "course_id": "01418497",
            "course_name": "Seminar",
            "student_grade": "B"
        }
    ],
    "student_cum_gpa": 3.95,
    "student_en_name": "Weerawong VONGGATUNYU",
    "student_en_title": "Mr.",
    "student_faculty": "Faculty Of Science",
    "student_id": "6410406860",
    "student_major": "Computer Science",
    "student_th_name": "วีรวงศ์ วงศ์กตัญญู",
    "student_th_title": "นาย"
}

result = check_graduation(student_data) # False

print(result)