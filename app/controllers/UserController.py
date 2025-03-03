from app.services import UserService

class UserController:
    def __init__(self):
        self.user_service = UserService()

    def get_user(self):
        return self.user_service.get_user()