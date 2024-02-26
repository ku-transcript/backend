from extract_pdf_text import extract_pdf_text
from parse_text import parse_text

def get_student_data(file):
  
  text = extract_pdf_text(file)
  data = parse_text(text)
  
  return data