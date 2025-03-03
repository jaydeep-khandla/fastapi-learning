from fastapi import APIRouter
from app.controllers import UserController

router = APIRouter()

user_controller = UserController()

router.get("/user/")(user_controller.get_user)