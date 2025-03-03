import os
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from contextlib import contextmanager

SQLALCHEMY_DATABASE_URL = os.getenv("SQLALCHEMY_DATABASE_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

@contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def check_sql_connection():
    try:
        with get_db() as db:
            # Try to execute a simple query
            db.execute(text('SELECT 1'))
            print("Successfully connected to SQL Database!")
        return True
    except Exception as e:
        print(f"Failed to connect to SQL Database: {e}")
        raise

def init_sql_db():
    try:
        # Create all tables stored in this metadata
        Base.metadata.create_all(bind=engine)
        print("SQL Database tables created successfully!")
    except Exception as e:
        print(f"Failed to initialize SQL Database: {e}")
        raise

mongodb_client = None

def get_mongodb_client():
    global mongodb_client
    if mongodb_client is None:
        mongodb_client = MongoClient(os.getenv("MONGODB_URI"), 
                                     server_api=ServerApi('1'),
                                     serverSelectionTimeoutMS=5000,
                                     connectTimeoutMS=5000)
    return mongodb_client

def get_mongodb_database():
    try:
        client = get_mongodb_client()
        db = client.fastdb
        # Test connection
        client.admin.command('ping')
        print("Successfully connected to MongoDB!")
        return db
    except Exception as e:
        print(f"Failed to connect to MongoDB: {e}")
        raise

def close_mongodb_client():
    global mongodb_client
    if mongodb_client:
        mongodb_client.close()
        mongodb_client = None
    
    
