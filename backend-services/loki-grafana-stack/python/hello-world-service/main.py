from fastapi import FastAPI
import logging
from log_handler import configure_logger
import json

app = FastAPI()

# Load configuration from JSON file
with open('./config/appsettings.json') as f:
    config = json.load(f)

# Check if the loki_url key exists in the config
if 'loki_url' in config:
    loki_url = config['loki_url']
else:
    loki_url = "http://192.168.99.100:3100/loki/api/v1/push"

# Create a logger
logger = logging.getLogger('python-hello-world-service-logger')
# Configure logger
configure_logger(logger, loki_url)

@app.get('/api/v1/hws', status_code=200)
async def hello():
    logger.info(
        "Hello, World from Python", 
        extra={"tags": {"service": "hello-world-service"}},
    )
    return { "message": "Hello, World from Python" } 
