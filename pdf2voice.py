import PyPDF2
import pyttsx3
import pdfplumber

# Name of the file
file = 'Test.pdf'

# Open and read file
pdfOpen = open(file, 'rb')
pdfReader = PyPDF2.PdfReader(pdfOpen)

# Get the number of pages 
getPages = len(pdfReader.pages)

finalText = ""

# Loop through the number of pages and extract the text 
with pdfplumber.open(file) as pdf:
    for i in range(0, getPages): 
        page = pdf.pages[i]
        text = page.extract_text()
        finalText += text

# Initialize the speech engine driver 
engine = pyttsx3.init()

# Save file into mp3 format 
engine.save_to_file(finalText, 'Test.mp3')
engine.runAndWait()