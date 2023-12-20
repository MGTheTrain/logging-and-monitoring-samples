FROM ubuntu:20.04 as builder
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && \
    apt-get install -y curl build-essential
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
WORKDIR /app/
COPY ./backend-services/prometheus-grafana-stack/rust/hello-world-service .
# Set the HOME environment variable (if it's not already set)
ENV HOME /root
# Add $HOME/.cargo/bin to the PATH environment variable
RUN echo 'export PATH="$HOME/.cargo/bin:$PATH"' >> ~/.bashrc
# Set the PATH for the current session
ENV PATH="/root/.cargo/bin:${PATH}"
RUN cargo build --release

FROM debian:bullseye-slim
WORKDIR /app/
RUN apt-get update
COPY --from=builder /app/target/release/hello-world-service .  
EXPOSE 80
RUN chmod +x hello-world-service
ENV RUST_LOG=debug
CMD ["./hello-world-service"]

# building the docker image on Unix systems from `cd ../../../../`: sudo docker build -t rust-hello-world-service:0.1.0 -f ./backend-services/prometheus-grafana-stack/rust/hello-world-service/Dockerfile .
# run the docker container on Unix systems: sudo docker run --rm -p 5004:80 -d rust-hello-world-service:0.1.0 