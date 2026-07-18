from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

DATABASE_URL="postgresql://postgres:divya@localhost:5432/mydatabase2"
engine=create_engine(DATABASE_URL)

sessionLocal=sessionmaker(autoflush=False,bind=engine)

Base=declarative_base()



