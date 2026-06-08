from typing import Optional
from fastapi import FastAPI, HTTPException, UploadFile, File
import logging

app = FastAPI()
logging.basicConfig(level=logging.INFO)

@app.post("/upload/")
async def pdf_upload(file: UploadFile = File(...)):
    content = await file.read()
    logging.info(f"Received file: {file.filename}, Size: {len(content)} bytes, Type: {file.content_type}")
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Invalid file type. Only PDF files are allowed.")
    
    return{
        "filename": file.filename,
        "size": len(content),
        "type": file.content_type
    }






