import os
from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.api.v1 import router
from app.config.db import get_mongodb_database, check_sql_connection, init_sql_db, close_mongodb_client, SessionLocal
from sqlalchemy.orm import Session

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup logic
    try:
        app.mongodb = get_mongodb_database()
        
        if check_sql_connection():
            init_sql_db()
        
        yield  
        
    finally:
        # Shutdown logic
        close_mongodb_client()
        print("Closing MongoDB connection")
        
        try:
            db: Session = SessionLocal()
            db.close()  # Close the SQL session
            print("SQL connection closed successfully.")
        except Exception as e:
            print(f"Error closing SQL connection: {e}")

app = FastAPI(lifespan=lifespan)

app.include_router(router)