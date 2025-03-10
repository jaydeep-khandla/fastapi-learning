from fastapi import Depends
from pydantic import BaseModel, Field
from app.models import Books
from app.config.db import engine, get_db
from sqlalchemy.orm import Session

# Books.metadata.create_all(bind=engine)
    
class BooksService:
    
    def create_book(self, book: Books, db: Session):
        # db = next(get_db())
        print(book)
        book_model = Books(
            title=book.title,
            author=book.author,
            year=book.year,
            genre=book.genre,
            price=book.price,
            rating=book.rating,
            description=book.description
        )
        db.add(book_model)
        db.commit()
        db.refresh(book_model)
        return book_model
    
    def list_books(self, db: Session):
        # db = next(self.get_db())
        return db.query(Books).all()