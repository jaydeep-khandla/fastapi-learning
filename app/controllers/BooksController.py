from app.services import BooksService
from app.schema import Book
from app.config.db import get_db
from fastapi import HTTPException
from sqlalchemy.orm import Session
from fastapi import Depends

class BooksController:
    
    def __init__(self):
        self.books_service = BooksService()

    def create_book(self, request: Book, db: Session = Depends(get_db)):
        try:
            created_book = self.books_service.create_book(request, db)
            return created_book
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error: {e}")

    def list_books(self, db: Session = Depends(get_db)):
        try:
            return self.books_service.list_books(db)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error: {e}")