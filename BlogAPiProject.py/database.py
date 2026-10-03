from sqlalchemy import create_engine # type: ignore
from sqlalchemy.orm import sessionmaker, declarative_base
 # pyright: ignore[reportMissingImports]

DATABASE_URL="postgresql+psycopg2://postgres:65641853@localhost:5432/fastApi"

engine=create_engine(DATABASE_URL)
SessionLocal=sessionmaker(bind=engine)
Base=declarative_base()