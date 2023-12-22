from fastapi import FastAPI, HTTPException
from jaeger_client import Config
from opentracing import tracer
import requests
import os

app = FastAPI()

def load_jaeger_configuration():
    # Add your logic to load Jaeger configuration, for example, from environment variables or a file
    jaeger_config = {
        'sampler': {
            'type': 'const',
            'param': 1,
        },
        'logging': True,
        'local_agent': {
            'reporting_host': os.getenv('JAEGER_HOST', '192.168.99.100'),
            'reporting_port': int(os.getenv('JAEGER_PORT', 6831)),
        },
    }
    return jaeger_config

def initialize_tracer():
    config = Config(
        config=load_jaeger_configuration(),
        service_name='hello-world-service',
        validate=True,
    )
    return config.initialize_tracer()

# Initialize the Jaeger tracer
tracer = initialize_tracer()

@app.get("/api/v1/hws")
def hello():
    with tracer.start_span('hello-world') as span:
        span.set_tag('http.method', 'GET')
        span.set_tag('http.url', '/api/v1/hws')
        span.set_tag('service.name', 'hello-world-service')

        # Logging key-value pairs
        span.log_kv({
            'message': 'Handling GET request for /api/v1/hws',
            'http.status_code': 200,
        })

        # Simulating an HTTP request to another service
        try:
            response = requests.get("http://example.com")
            return { "message": "Hello, World from Python" }
        except Exception as e:
            span.log_kv({'error': str(e)})
            raise HTTPException(status_code=500, detail="Service unavailable")

@app.on_event("shutdown")
async def on_shutdown():
    tracer.close()
