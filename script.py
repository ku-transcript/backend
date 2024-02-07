from PyPDF2 import PdfReader 
# import PyPDF2
import re
import urllib.request
import io

def getStudentCoursesFromPDF(file):
  reader = PdfReader(file)
  courses = []

  # getting a specific page from the pdf file 
  for i in range(len(reader.pages)):
      page = reader.pages[i] 
      # extracting text from page 
      text = page.extract_text() 

      matches = re.findall(r"([A-D][+]?|[FPNW]) (\d{1}) ([\w ]+) (\d{8})", text, re.MULTILINE)
      name = re.findall(r"(Miss|Mr\.) ([\w ]+ [\w ]+)", text, re.MULTILINE)[0]
      major = re.findall(r"(Field Of Study) ([\w ]+) (Miss|Mr\.)", text, re.MULTILINE)[0][1]
      
      for match in matches:
          student_grade, course_credit, course_name, course_id = match
          courses.append({
            "student_grade": student_grade,
            "course_credit": course_credit,
            "course_name": course_name,
            "course_id": course_id
          })

          print(student_grade, course_credit, course_name, course_id)
  
  return courses
  
# # Read PDF file remotely
# URL = 'https://cdn.glitch.global/b47f022b-8699-4b00-bf3c-d2513ddf3842/STD_GRADE_REPORT_6410406860.pdf?v=1707336428329'
# req = urllib.request.Request(URL, headers={'User-Agent' : "Magic Browser"})
# remote_file = urllib.request.urlopen(req).read()
# remote_file_bytes = io.BytesIO(remote_file)