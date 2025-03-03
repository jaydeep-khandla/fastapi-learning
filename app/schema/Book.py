# app/schema/Book.py
from pydantic import BaseModel, Field

class Book(BaseModel):
    title: str = Field( min_length=1, max_length=100, description="Title of the book")
    author: str = Field( min_length=1, max_length=100, description="Author of the book")
    year: int = Field( description="Year of the book")
    genre: str = Field( min_length=1, max_length=50, description="Genre of the book")
    price: int = Field( description="Price of the book")
    rating: int = Field( description="Rating of the book")
    description: str = Field( min_length=1, max_length=500, description="Description of the book")
    
    class Config:
        from_attributes = True
