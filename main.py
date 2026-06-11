from fastapi import FastAPI
import logging
import httpx

app=FastAPI()
logging.basicConfig(level=logging.INFO)

@app.get("/todo")
async def get_todo():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://jsonplaceholder.typicode.com/todos/1")
    return response.json()
    return response.status_code
    
	





