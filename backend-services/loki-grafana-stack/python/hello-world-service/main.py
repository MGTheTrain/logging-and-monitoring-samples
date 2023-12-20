from fastapi import FastAPI
import logging
from log_handler import configure_logger
import json
from datetime import datetime

app = FastAPI()

# Load configuration from JSON file
with open('./config/appsettings.json') as f:
    config = json.load(f)

# Check if the loki_url key exists in the config
if 'loki_url' in config:
    loki_url = config['loki_url']
else:
    loki_url = "http://192.168.99.100:3100/loki/api/v1/push"
    # It's preferable to verify the existence of an environment variable and utilize it rather than relying on a fixed, hardcoded value. E.g.
    # import os
    # loki_url = os.getenv('LOKI_URL')
    # if loki_url:
    #     print(f"LOKI_URL is set to: {loki_url}")
    # else:
    #     print("LOKI_URL is not set")

# Create a logger
logger = logging.getLogger('python-hello-world-service-logger')
# Configure logger
configure_logger(logger, loki_url)

@app.get('/api/v1/hws', status_code=200)
async def hello():
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"[{current_datetime}] Hello, World from Python"
    
    logger.info(
        log_message, 
        extra={"tags": {"service": "hello-world-service"}},
    )
    return { "message": "Hello, World from Python" } 
