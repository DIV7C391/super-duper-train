from fastapi import FastAPI

app = FastAPI()

@app.get("/books")
def get_books():
    return [
        {
            "id": 1,
            "title": "FastAPI Basics"
        },
        {
            "id": 2,
            "title": "Building AI Agents"
        }
    ]

