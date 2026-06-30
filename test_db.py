from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import engine
from sqlalchemy import text
DATABASE_URL="postgresql://postgres:divya@localhost:5432/mydatabase"
engine=create_engine(DATABASE_URL)
sessionLocal=sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
    )
with engine.connect() as conn:
    result=conn.execute(text("SELECT 1"))
    print(result.fetchone())