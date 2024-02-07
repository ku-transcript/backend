from PyPDF2 import PdfReader 
import re
  
# creating a pdf reader object 
reader = PdfReader('/public/STD_GRADE_REPORT_6410406860.pdf') 
  
# printing number of pages in pdf file 
print(len(reader.pages)) 
  
courses = []

# getting a specific page from the pdf file 
for i in range(len(reader.pages)):
    page = reader.pages[i] 
    # extracting text from page 
    text = page.extract_text() 

    matches = re.findall(r"([A-D][+]?|[FPNW]) (\d{1}) ([\w ]+) (\d{8})", text, re.MULTILINE)

    for match in matches:
        courses.append(match)
    
    print(text) 

for course in courses:
    print(course)