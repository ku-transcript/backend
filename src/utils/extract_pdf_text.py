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


# # Read PDF file remotely
# URL = 'https://cdn.glitch.global/b47f022b-8699-4b00-bf3c-d2513ddf3842/STD_GRADE_REPORT_6410406860.pdf?v=1707336428329'
# req = urllib.request.Request(URL, headers={'User-Agent' : "Magic Browser"})
# remote_file = urllib.request.urlopen(req).read()
# remote_file_bytes = io.BytesIO(remote_file)