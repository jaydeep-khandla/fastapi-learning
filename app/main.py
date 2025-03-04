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
    app.mongodb = None  # Ensure MongoDB instance is tracked
    app.sql_db_session = None  # Track the SQLAlchemy session

    try:
        print("Starting application...")

        # 1️⃣ **Initialize MongoDB Connection**
        try:
            app.mongodb = get_mongodb_database()
            print("MongoDB connected successfully.")
        except Exception as e:
            print(f"MongoDB connection failed: {e}")
            raise RuntimeError("MongoDB connection failed. Server will not start.")  # Stop FastAPI

        # 2️⃣ **Check SQL Database Connection**
        if not check_sql_connection():
            raise RuntimeError("SQL Database connection failed. Server will not start.")  # Stop FastAPI
        
        # 3️⃣ **Initialize SQL Database**
        init_sql_db()
        print("SQL Database initialized.")

        # 4️⃣ **Create and Store SQLAlchemy Session for Cleanup**
        app.sql_db_session = SessionLocal()

        yield  # 🔥 FastAPI app starts here

    finally:
        print("Shutting down application...")

        # 🛑 **Close MongoDB Connection**
        close_mongodb_client()
        print("MongoDB connection closed.")

        # 🛑 **Close SQLAlchemy Session (If Open)**
        if app.sql_db_session:
            try:
                app.sql_db_session.close()
                print("SQLAlchemy session closed successfully.")
            except Exception as e:
                print(f"Error closing SQL connection: {e}")

app = FastAPI(lifespan=lifespan)

app.include_router(router)