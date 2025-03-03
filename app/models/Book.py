from sqlalchemy import Column, Integer, String
from app.config.db import Base

class Books(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), index=True)  # Specify length for VARCHAR
    author = Column(String(255))  # Specify length for VARCHAR
    year = Column(Integer)
    genre = Column(String(255))  # Specify length for VARCHAR
    price = Column(Integer)
    rating = Column(Integer)
    description = Column(String(500))  