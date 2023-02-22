from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse

app = FastAPI()
app.title = 'FastAPI app'
app.version = '0.0.1'

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
def create_movie(id: int = Body(), title: str = Body(), overview: str = Body(), year: int = Body(), rating: int = Body(), category: str = Body()):
    movies.append({
        'id': id,
        'title': title,
        'overview': overview,
        'year': year,
        'rating': rating,
        'category': category
    })
    return movies

@app.put('/movies/{id}', tags=['movies'])
def update_movie(id: int, title: str = Body(), overview: str = Body(), year: int = Body(), rating: int = Body(), category: str = Body()):
	for item in movies:
		if item["id"] == id:
			item['title'] = title
			item['overview'] = overview
			item['year'] = year
			item['rating'] = rating
			item['category'] = category
			return movies