from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel

Base=declarative_base()

class Movielist(Base):
    __tablename__="movies"

    id=Column(Integer, primary_key=True, index=True)
    name=Column(String, primary_key=True, index=True)
    rating=Column(Integer, index=True)
    comment=Column(String, index=True)
    intro=Column(String, index=True)

SQLALCHEMY_DATABASE_URL="sqlite:///./test.db"
engine=create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal=sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

class Movie(BaseModel):
    name: str
    rating: int
    comment: str
    intro: str

app=FastAPI()

@app.get("/")
async def read_root():
    return {"message":"Hello, World!"}