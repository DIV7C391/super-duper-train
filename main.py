from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import asyncio

app = FastAPI()


async def resp():
    words = [
        "RAG ","stands ","for ","Retrieval ","Augmented ","Generation"]
    for word in words:

        yield word

        await asyncio.sleep(0.5)

@app.get("/stream")
async def response():
    return StreamingResponse(
        resp(),
        media_type="text/plain"
    )