from fastapi import FastAPI

app = FastAPI()


@app.get("/about")
def about():
    return {
        "message": "About Page"
    }