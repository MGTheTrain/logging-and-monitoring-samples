from fastapi import FastAPI, HTTPException, status
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()
Instrumentator().instrument(app).expose(app)

@app.get('/api/v1/hws', status_code=200)
async def hello():
    return { "message": "Hello, World from Python" } 