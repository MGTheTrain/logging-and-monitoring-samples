FROM alpine:latest AS builder

WORKDIR /app
COPY ./backend-services/prometheus-grafana-stack/go/hello-world-service .

RUN /bin/sh -c "apk add --no-cache go && \
                go mod tidy && \
                go build -o hello-word-service ."

FROM alpine:latest
WORKDIR /app
COPY --from=builder /app/hello-word-service .
EXPOSE 80
ENTRYPOINT ["./hello-word-service"]

# building the docker image on Unix systems from `cd ../../../../`: sudo docker build -t go-hello-world-service:0.1.0 -f ./backend-services/prometheus-grafana-stack/go/hello-world-service/Dockerfile .
# run a docker container on Unix systems: sudo docker run --rm -p 5002:80 -d go-hello-world-service:0.1.0 