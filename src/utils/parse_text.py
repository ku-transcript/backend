import re
from datetime import datetime


COURSES_REGEX = r"([A-D][+]?|[FPNW]) (\d{1}) (.+) (\d{8})"
EN_NAME_REGEX = r"(Miss|Mr\.) ([\w ]+ [\w ]+)"
TH_NAME_REGEX = r"(^น\w+) (.+)"
MAJOR_REGEX = r"(Field Of Study) ([\w ]+) (Miss|Mr\.)"
STUDENT_NO_FACULTY_REGEX = r"Student No (\d+) ([\w ]+)"
CUM_GPA_REGEX = r"cum G.P.A. = (\d+(?:\.\d+)?)"
DOA_REGEX = r"Date Of Admission ((?:January|February|March|April|May|June|July|August|September|October|November|December)   \d{1,2}, \d{4})"


def parse_text(text):
  data = dict()
  courses = []
  
  matches = re.findall(COURSES_REGEX, text, re.MULTILINE)
  en_title, en_name = re.findall(EN_NAME_REGEX, text, re.MULTILINE)[0]
  th_title, th_name = re.findall(TH_NAME_REGEX, text, re.MULTILINE)[0]
  major = re.findall(MAJOR_REGEX, text, re.MULTILINE)[0][1]
  student_no, faculty = re.findall(STUDENT_NO_FACULTY_REGEX, text, re.MULTILINE)[0]
  cum_gpa = re.findall(CUM_GPA_REGEX, text, re.MULTILINE)[-1]
  date_of_admission = re.findall(DOA_REGEX, text, re.MULTILINE)[0]
    
  data['student_id'] = student_no
  data['student_en_title'] = en_title
  data['student_en_name'] = en_name
  data['student_th_title'] = th_title
  data['student_th_name'] = th_name
  data['student_faculty'] = faculty
  data['student_major'] = major
  data['student_cum_gpa'] = float(cum_gpa)
  data['date_of_admission'] = datetime.strptime(date_of_admission, '%B %d, %Y')

  for match in matches:
      student_grade, course_credit, course_name, course_id = match
      courses.append({
        "student_grade": student_grade,
        "course_credit": int(course_credit),
        "course_name": course_name,
        "course_id": course_id
      })

      # print(student_grade, course_credit, course_name, course_id)

  data['enrolled_courses'] = courses

  return data