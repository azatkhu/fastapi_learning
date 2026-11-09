from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase


BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "students.db"

engine = create_engine(
    f"sqlite:///{DB_PATH}",
)

SessionLocal = sessionmaker(bind = engine)

class Base(DeclarativeBase):
    pass

def get_db():
    db = SessionLocal()
    
    try:
        yield db
        
    finally:
        db.close()
        