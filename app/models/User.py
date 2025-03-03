from pydantic import BaseModel

class User(BaseModel):
    name: str = ""
    age: int = None
    email: str = ""
    is_active: bool = False