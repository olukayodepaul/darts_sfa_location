from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from connection.connect_config import config

from sqlalchemy import text

DB_USER = config['ps_sql']['ps_user']
DB_PASSWORD = config['ps_sql']['ps_password']
DB_HOST = config['ps_sql']['ps_host_name']
DB_PORT = config['ps_sql']['ps_port']
DB_NAME = config['ps_sql']['ps_db']

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
    

