from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import logging
import httpx

app=FastAPI()
logging.basicConfig(level=logging.INFO)

class ChatRequest(BaseModel):
    message: str=Field(min_length=1, max_length=2000)

class ChatResponse(BaseModel):
    answer:str

@app.post("/chat",response_model=ChatResponse)

async def ask_llm(data:ChatRequest):

    return {
        "answer": f"You asked: {data.message}"
    }

@app.post("/chat",response_model=ChatResponse)
async def chat(data:ChatRequest):
    try:
        answer= await ask_llm(data.message)
        return {
            "answer": answer
        }
    except Exception:
        raise HTTPException(status_code=500, detail= "AI service unavailable")




	





