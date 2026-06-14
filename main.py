from fastapi import FastAPI,Header, HTTPException
from fastapi.responses import StreamingResponse
import asyncio


app = FastAPI()

@app.get("/admin")
async def protected(X_API_KEY: str = Header()):
    if X_API_KEY!="secret123":
        raise HTTPException(status_code=401, detail="invalid api key")
    else:
        return{
            "message":"access granted"
        }