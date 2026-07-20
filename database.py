from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Session

DATABASE_URL="postgresql://postgres:divya@localhost:5432/mydatabase3"
engine=create_engine(DATABASE_URL)

sessionLocal=sessionmaker(autoflush=False,bind=engine)

Base=declarative_base()

def get_db():
    db=sessionLocal()
    try:
        yield db
    finally:
        db.close()


    





