from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQLALCHEMY_DATABASE_URI = "sqlite:///db.sqlite3"

# Create An Engine
engine = create_engine(SQLALCHEMY_DATABASE_URI, connect_args={"check_same_thread": False}, echo=True, future=True)

# Create A Configured "Local Session" sessionmaker Class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create A Declarative Base Class
Base = declarative_base()