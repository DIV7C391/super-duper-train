from typing import Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import os
import logging

logging.basicConfig(level=logging.INFO)

app = FastAPI()
@app.post("/")
def home():
    try:

        response=openai_call("Hello, world!")
        return response
    
        logging.info("loaded")

    except Exception as e:
    
        logging.error("REQUEST FAILED")
        raise HTTPException(status_code=500, detail="server error")



