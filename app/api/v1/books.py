from fastapi import APIRouter
from app.controllers import BooksController

router = APIRouter()

books_controller = BooksController()

router.post("/create-book/")(books_controller.create_book)

router.get("/list-books/")(books_controller.list_books)