from fastapi import FastAPI, HTTPException, status
import logging
import logging_loki

app = FastAPI()
handler = logging_loki.LokiHandler(
    url="https://my-loki-instance/loki/api/v1/push", 
    tags={"application": "python-hello-world-service"},
    # auth=("username", "password"),
    version="1",
)

logger = logging.getLogger("hello-world-service-logger")
logger.addHandler(handler)

@app.get('/api/v1/hws', status_code=200)
async def hello():
    logger.info(
        { "message": "Hello, World from Python" }, 
        extra={"tags": {"service": "hello-world-service"}},
    )
    return { "message": "Hello, World from Python" } 