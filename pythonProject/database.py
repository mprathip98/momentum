from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

# Replace with your actual Neon DB URL
DATABASE_URL = os.getenv("DATABASE_URL") or "postgresql+psycopg2://your_user:your_password@your_neon_host/db_name"

engine = create_engine(DATABASE_URL, echo=True)

# Session maker bound to this engine
SessionLocal = sessionmaker(bind=engine)
