from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()
app.title = 'FastAPI app'
app.version = '0.0.1'

class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=3, max_length=50)
    overview: str = Field(min_length=3, max_length=150)
    year: int = Field(le=2023)
    rating: float
    category: str

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

@app.get('/movies', tags=['movies'])
def get_movies():
    return movies

@app.get('/movies/{id}', tags=['movies'])
def get_movie(id: int):
    for item in movies: 
        if item["id"] == id: return item
    
    return []

@app.get('/movies/', tags=['movies'])
def get_movies_by_category(category: str):
    # data = []
    # for item in movies: 
    #     if item["category"] == category: 
    #         data.append(item)
    # return data
    return [item for item in movies if item['category'] == category]

@app.post('/movies/', tags=['movies'])
# def create_movie(id: int = Body(), title: str = Body(), overview: str = Body(), year: int = Body(), rating: int = Body(), category: str = Body()):
#     movies.append({
#         'id': id,
#         'title': title,
#         'overview': overview,
#         'year': year,
#         'rating': rating,
#         'category': category
#     })
def create_movie(movie: Movie):
    movies.append(movie)
    return movies

@app.put('/movies/{id}', tags=['movies'])
def update_movie(id: int, movie: Movie):
	for item in movies:
		if item["id"] == id:
			item['title'] = movie.title
			item['overview'] = movie.overview
			item['year'] = movie.year
			item['rating'] = movie.rating
			item['category'] = movie.category
			return movies

@app.delete('/movies/{id}', tags=['movies'])
def delete_movie(id: int):
    for item in movies:
        if item["id"] == id:
            movies.remove(item)
            return item