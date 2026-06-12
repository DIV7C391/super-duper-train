 
            
from fastapi import FastAPI
from fastapi import HTTPException, UploadFile, File
from pypdf import PdfReader
import tempfile
import logging

app=FastAPI()
logging.basicConfig(level=logging.INFO)

@app.post("/pdf-info")
async def info_pdf(file: UploadFile = File(...)):
    #if file.content_type != "application/pdf":
        #raise HTTPException(status_code=400, detail="Invalid file type. Only PDF files are allowed.")
    logging.info("pdf loading")
    content= await file.read()
    with tempfile.NamedTemporaryFile(delete=False,suffix=".pdf") as temp_file:
        temp_file.write(content)
        
    try:
        reader=PdfReader(temp_file.name)
    except Exception as e:
        logging.error(f"Error reading PDF: {e}")
        raise HTTPException(status_code=400, detail="Invalid PDF file.")
    
    pages=len(reader.pages)
    char=0
    text=""
    for page in reader.pages:
        char1=page.extract_text()
        text+=char1
        char+=len(char1)
    
    return {
        "filename": file.filename,
        "pages": pages,
        "characters": char,
        "text": text
     
    }

