from fastapi import FastAPI

app = FastAPI()
app.title = "FastAPI app"
app.version = "0.0.1"

@app.get("/", tags=["home"])

def message():
    return "hello world!"