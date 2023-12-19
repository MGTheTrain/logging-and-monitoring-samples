from fastapi import FastAPI, HTTPException, status

app = FastAPI()

@app.get('/api/v1/hws', status_code=200)
async def hello():
    return { "message": "Hello, World from Python" } 