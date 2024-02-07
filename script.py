from PyPDF2 import PdfReader 
import re
import urllib.request
import io

# TODO: check if file is a transcript
def get_student_data(file):
  reader = PdfReader(file)
  text = ''
  
  # getting a specific page from the pdf file 
  for i in range(len(reader.pages)):
      page = reader.pages[i] 
      # extracting text from page 
      text += page.extract_text() 

  data = clean_up_text(text)
  
  # TODO: if student's major is not CS throw error (Currently support only CS major)

  return data

def clean_up_text(text):
  data = dict()
  courses = []
  
  matches = re.findall(r"([A-D][+]?|[FPNW]) (\d{1}) ([\w ]+) (\d{8})", text, re.MULTILINE)
  en_title, en_name = re.findall(r"(Miss|Mr\.) ([\w ]+ [\w ]+)", text, re.MULTILINE)[0]
  th_title, th_name = re.findall(r"(^น\w+) (.+)", text, re.MULTILINE)[0]
  major = re.findall(r"(Field Of Study) ([\w ]+) (Miss|Mr\.)", text, re.MULTILINE)[0][1]
  student_no, faculty = re.findall(r"Student No (\d+) ([\w ]+)", text, re.MULTILINE)[0]

  data['student_id'] = student_no
  data['student_en_title'] = en_title
  data['student_en_name'] = en_name
  data['student_th_title'] = th_title
  data['student_th_name'] = th_name
  data['student_faculty'] = faculty
  data['student_major'] = major

  for match in matches:
      student_grade, course_credit, course_name, course_id = match
      courses.append({
        "student_grade": student_grade,
        "course_credit": course_credit,
        "course_name": course_name,
        "course_id": course_id
      })

      print(student_grade, course_credit, course_name, course_id)

  data['enrolled_courses'] = courses

  return data
  
  
# # Read PDF file remotely
# URL = 'https://cdn.glitch.global/b47f022b-8699-4b00-bf3c-d2513ddf3842/STD_GRADE_REPORT_6410406860.pdf?v=1707336428329'
# req = urllib.request.Request(URL, headers={'User-Agent' : "Magic Browser"})
# remote_file = urllib.request.urlopen(req).read()
# remote_file_bytes = io.BytesIO(remote_file)