from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()
app.title = 'FastAPI app'
app.version = '0.0.1'

movies = [
    {
        "id": 1,
        "title": "Avatar",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        "year": "2009",
        "rating": 7.8,
        "category": "Acción"
    },
    {
        "id": 2,
        "title": "Avatar 2",
        "overview": "...",
        "year": "20XX",
        "rating": "X",
        "category": "Acción"
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