from fastapi import FastAPI, HTTPException, Depends
import mysql.connector
from pydantic import BaseModel

app = FastAPI()

DATABASE_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'online_library_db'
}


class Book(BaseModel):
    title: str
    author: str


def get_db():
    db = mysql.connector.connect(**DATABASE_CONFIG)
    cursor = db.cursor(dictionary=True)
    return db, cursor


@app.get("/books/")
def read_books(db: mysql.connector.MySQLConnection = Depends(get_db)):
    db, cursor = db
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    cursor.close()
    db.close()
    return books


@app.get("/books/{book_id}")
def read_book(book_id: int, db: mysql.connector.MySQLConnection = Depends(get_db)):
    db, cursor = db
    cursor.execute("SELECT * FROM books WHERE id=%s", (book_id,))
    book = cursor.fetchone()
    cursor.close()
    db.close()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@app.post("/books/")
def create_book(book: Book, db: mysql.connector.MySQLConnection = Depends(get_db)):
    db, cursor = db
    cursor.execute("INSERT INTO books (title, author) VALUES (%s, %s)", (book.title, book.author))
    db.commit()
    book_id = cursor.lastrowid
    cursor.close()
    db.close()
    return {"id": book_id, **book.model_dump()}


@app.put("/books/{book_id}")
def update_book(book_id: int, book: Book, db: mysql.connector.MySQLConnection = Depends(get_db)):
    db, cursor = db
    cursor.execute("UPDATE books SET title=%s, author=%s WHERE id=%s", (book.title, book.author, book_id))
    db.commit()
    updated_rows = cursor.rowcount
    cursor.close()
    db.close()
    if updated_rows == 0:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"id": book_id, **book.model_dump()}


@app.delete("/books/{book_id}")
def delete_book(book_id: int, db: mysql.connector.MySQLConnection = Depends(get_db)):
    db, cursor = db
    cursor.execute("DELETE FROM books WHERE id=%s", (book_id,))
    db.commit()
    deleted_rows = cursor.rowcount
    cursor.close()
    db.close()
    if deleted_rows == 0:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"status": "successful", "message": "Book deleted"}
