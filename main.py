from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class AskQues(BaseModel):
    user: str
    message: str

# {document_id} is a path parameter
@app.post("/ask-document/{document_id}")
def give_ans(
    document_id: str,                 # Captures from the URL path
    ans: AskQues,                     # Captures from the JSON body
    detail_level: str = "short",      # Query parameter (default: "short")
    include_citations: bool = True     # Query parameter (default: True)
):  
    return {
        "document_id": document_id,
        "received_from": ans.user,
        "question": ans.message,
        "config": {
            "detail_level": detail_level,
            "include_citations": include_citations
        },
        "reply": f"Answering '{ans.message}' for document {document_id}."
    }

