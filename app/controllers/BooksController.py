from app.services import BooksService
from app.schema import Book
from fastapi import HTTPException

class BooksController:
    def __init__(self):
        self.books_service = BooksService()

    def create_book(self, request: Book):
        
        try:
            created_book = self.books_service.create_book(request)
            return created_book
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error: {e}")

    def list_books(self):
        return self.books_service.list_books()