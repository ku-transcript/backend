from PyPDF2 import PdfReader 

def extract_pdf_text(file):
  reader = PdfReader(file)
  text = ''
  
  # getting a specific page from the pdf file 
  for i in range(len(reader.pages)):
      page = reader.pages[i] 
      # extracting text from page 
      text += page.extract_text() 
  
  print(text)
  
  return text