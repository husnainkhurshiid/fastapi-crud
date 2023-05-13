from fastapi import FastAPI, HTTPException
from models.book import Book
from uuid import UUID

app = FastAPI()

BOOKS = []


@app.get("/")
def read_api():
    return BOOKS


@app.post("/")
def create_book(book: Book):
    BOOKS.append(book)
    return book


@app.put("/{book_id}")
def update_book(book_id: UUID, book: Book):
    counter = 0

    for x in BOOKS:
        counter += 1
        if x.id == book_id:
            BOOKS[counter - 1] = book
            return BOOKS[counter - 1]
    raise HTTPException(
        status_code=404,
        detail=f"ID {book_id} : Does not exist"
    )


@app.delete("/{book_id}")
def delete_book(book_id: UUID):
    counter = 0

    for x in BOOKS:
        counter += 1
        if x.id == book_id:
            del BOOKS[counter - 1]
            return f"ID: {book_id} deleted"
    raise HTTPException(
        status_code=404,
        detail=f"ID {book_id} : Does not exist"
    )