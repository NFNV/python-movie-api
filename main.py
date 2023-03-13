from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from config.database import engine, Base
from middlewares.error_handler import ErrorHandler
from routes.movie import movie_router
from routes.user import user_router

app = FastAPI(title='FastAPI app', version='0.0.1')

app.add_middleware(ErrorHandler)

app.include_router(movie_router)

app.include_router(user_router)

Base.metadata.create_all(bind=engine)

movies = [
    {
        "id": 1,
        "title": "Avatar",
        "overview": "...",
        "year": 2009,
        "rating": 7.9,
        "category": "action"
    },
    {
        "id": 2,
        "title": "Avatar: The Way of Water",
        "overview": "...",
        "year": 2022,
        "rating": 7.8,
        "category": "action"
    },
]

@app.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1>Hello world!</h1>')