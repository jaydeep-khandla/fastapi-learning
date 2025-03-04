from app.services import BooksService
from app.schema import Book
from app.config.db import get_db
from fastapi import HTTPException
from sqlalchemy.orm import Session
from fastapi import Depends

class BooksController:

    def create_book(self, request: Book, db: Session = Depends(get_db)):
        books_service = BooksService(db)
        
        try:
            created_book = books_service.create_book(request)
            return created_book
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error: {e}")

    def list_books(self, db: Session = Depends(get_db)):
        books_service = BooksService(db)
        try:
            return books_service.list_books()
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error: {e}")