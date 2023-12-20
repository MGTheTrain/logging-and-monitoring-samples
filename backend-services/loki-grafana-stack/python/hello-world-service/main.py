from fastapi import FastAPI, HTTPException, status
import logging
import logging_loki
logging_loki.emitter.LokiEmitter.level_tag = "level"

app = FastAPI()

# Create a logger
logger = logging.getLogger('python-hello-world-service-logger')
logger.setLevel(logging.DEBUG)
# Replace with your Loki server URL and port
loki_url = 'http://192.168.99.100:3100/loki/api/v1/push'
# Create a LokiHandler and set its URL
loki_handler = logging_loki.LokiHandler(
    url=loki_url,
    tags={"application": "python-hello-world-service"},
    version="1",
)
# Add the LokiHandler to the logger
logger.addHandler(loki_handler)

@app.get('/api/v1/hws', status_code=200)
async def hello():
    logger.info(
        "Hello, World from Python", 
        extra={"tags": {"service": "hello-world-service"}},
    )
    return { "message": "Hello, World from Python" } 