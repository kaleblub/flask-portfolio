from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Tell Where To Save The Database
# SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

# Create An Engine
def startEngine(uri):
	return create_engine(uri, connect_args={"check_same_thread": False})

# Create A Configured "Local Session" Class
def startLocalSession(engine):
	return sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create A Declarative Base Class
Base = declarative_base()
