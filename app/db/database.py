from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Ajusta estos valores a tu entorno MySQL
USER = "root"
PASSWORD = "admin"
HOST = "localhost"
PORT = "3306"
DB_NAME = "mydb"

DATABASE_URL = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL, echo=True, future=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
