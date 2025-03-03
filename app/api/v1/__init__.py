# from books import router as books_router
from fastapi import APIRouter

router = APIRouter()

from .users import router as users_router   
from .books import router as books_router
 
# router.include_router(books_router, prefix="/books", tags=["books"])
router.include_router(users_router, prefix="", tags=["users"])
router.include_router(books_router, prefix="/books", tags=["books"])