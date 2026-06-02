from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Home"
    }

@app.get("/about")
def about():
    return {
        "message": "About Page"
    }