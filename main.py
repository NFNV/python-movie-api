from fastapi import FastAPI, Body, Path, Query
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List

app = FastAPI(title='FastAPI app', version='0.0.1')

class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(..., min_length=3, max_length=50)
    overview: str = Field(..., min_length=3, max_length=150)
    year: int = Field(..., le=2023)
    rating: float = Field(..., ge=1, le=10)
    category: str = Field(..., min_length=3, max_length=15)

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "title": "My movie",
                "overview": "My description",
                "year": 2023,
                "rating": 7.0,
                "category": "action"
            }
        }

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

@app.get('/movies', tags=['movies'], response_model=List[Movie])
def get_movies() -> List[Movie]:
    return JSONResponse(content=movies)

@app.get('/movies/{id}', tags=['movies'], response_model=Movie)
def get_movie(id: int = Path(..., ge=1, le=20000)) -> Movie:
    for item in movies:
        if item["id"] == id:
            return JSONResponse(content=item)
    return JSONResponse(content=[])

@app.get('/movies/', tags=['movies'], response_model=List[Movie])
def get_movies_by_category(category: str = Query(..., min_length=3, max_length=15)) -> List[Movie]:
    data = [item for item in movies if item['category'] == category]
    return JSONResponse(content=data)

@app.post('/movies/', tags=['movies'], response_model=dict)
def create_movie(movie: Movie) -> dict:
    movies.append(movie.dict())
    return JSONResponse(content={'message': 'Movie created'})

@app.put('/movies/{id}', tags=['movies'], response_model=dict)
def update_movie(id: int, movie: Movie) -> dict:
    for item in movies:
        if item["id"] == id:
            item.update(movie.dict())
            return JSONResponse(content={'message': 'Movie modified'})
    return JSONResponse(content={'message': 'Movie not found'})

@app.delete('/movies/{id}', tags=['movies'], response_model=dict)
def delete_movie(id: int) -> dict:
    for item in movies:
        if item['id'] == id:
            movies.remove(item)
            return JSONResponse(content={'message': 'Movie deleted'})
    return JSONResponse(content={'message': 'Movie not found'})
