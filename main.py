from fastapi import FastAPI, HTTPException

app = FastAPI()

books_db=[{"id": 1, "title": "The Hobbit", "genre": "fantasy", "price": 14.99},
    {"id": 2, "title": "Dune", "genre": "sci-fi", "price": 19.99},
    {"id": 3, "title": "Foundation", "genre": "sci-fi", "price": 12.50},
    {"id": 4, "title": "Harry Potter", "genre": "fantasy", "price": 24.99},
    {"id": 5, "title": "Neuromancer", "genre": "sci-fi", "price": 10.99},]

@app.get("/books/{book_id}")
def get_book_by_id(book_id:int):
    for book in books_db:
        if book["id"]==book_id:
            return book
    
    raise HTTPException(status_code=404, detail="resource not found")


@app.get("/books")
def get_books(genre:str):
    for book in books_db:
        if book["genre"]==genre:
            return book
        
        else:
            return "NO such Genre"

    
    