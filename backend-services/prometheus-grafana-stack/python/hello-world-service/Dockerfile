FROM alpine:latest
WORKDIR /app
COPY ./backend-services/prometheus-grafana-stack/python/hello-world-service .

RUN apk add --no-cache python3 py3-pip

# Create a Python virtual environment and activate it
RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"

RUN /bin/sh -c "pip install --upgrade pip && \
                pip install -r requirements.txt"

ENTRYPOINT [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80" ]
EXPOSE 80

# Building the docker image from `cd ../../../../`: docker build -t python-hello-world-service:0.1.0 -f ./backend-services/prometheus-grafana-stack/python/hello-world-service/Dockerfile .
# Run the docker container: docker run --rm -p 5003:80 -d python-hello-world-service:0.1.0 