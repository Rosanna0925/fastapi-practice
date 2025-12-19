from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel

SQLALCHEMY_DATABASE_URL="sqlite:///./test.db"
engine=create_engine(SQLALCHEMY_DATABASE_URL)
Sesssional=sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base=declarative_base()

class Movie(Base):
    __tablename__="movies"

    id=Column(Integer, primary_key=True, index=True)
    name=Column(String, index=True)
    intro=Column(String, index=True)
    rating=Column(Integer, index=True)

Base.metadata.create_all(bind=engine)


movie_1=Movie(name="My sister's host", intro="touched movie!", rating=6)

with Session(engine) as session:
    session.add(movie_1)
    session.commit()
    session.refresh(movie_1)

app=FastAPI()

templates=Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    movies=Movie.query.all()
    return templates.TemplateResponse(
        request=request, name="index.html", movies=movies)