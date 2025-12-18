from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel

Base=declarative_base()

class MovieDB(Base):
    __tablename__="movies"

    id=Column(Integer, primary_key=True, index=True)
    name=Column(String, primary_key=True, index=True)
    intro=Column(String, index=True)
    rating=Column(Integer, index=True)

SQLALCHEMY_DATABASE_URL="sqlite:///./test.db"
engine=create_engine(SQLALCHEMY_DATABASE_URL)
Sesssional=sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Movie(BaseModel):
    name:str
    intro:str
    rating:int

app=FastAPI()

templates=Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html")