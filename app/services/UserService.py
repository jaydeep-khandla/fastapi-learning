from pydantic import BaseModel, Field

class User(BaseModel):
    id: str = Field(alias="user_id")
    name: str = Field(alias="user_name", min_length=1, max_length=15, description="Name of the user")
    email: str = Field(alias="user_email", min_length=1, max_length=15, description="Email of the user")
    
    class Config:
        populate_by_name = True

class UserService:
    def get_user(self):
        return User(id="1", name="John", email="john.doe@jd.com")