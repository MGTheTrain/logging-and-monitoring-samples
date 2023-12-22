FROM alpine:latest
WORKDIR /app
COPY ./backend-services/jaeger/python/hello-world-service .

RUN apk add --no-cache python3 py3-pip

# Create a Python virtual environment and activate it
RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"

RUN /bin/sh -c "pip install --upgrade pip && \
                pip install -r requirements.txt"

ENTRYPOINT [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80" ]
EXPOSE 80

# building the docker image on Unix systems from `cd ../../../../`: sudo docker build -t python-hello-world-service-with-jaeger:0.1.0 -f ./backend-services/jaeger/python/hello-world-service/Dockerfile .
# run the docker container on Unix systems: sudo docker run --rm -p 5003:80 -d python-hello-world-service-with-jaeger:0.1.0 