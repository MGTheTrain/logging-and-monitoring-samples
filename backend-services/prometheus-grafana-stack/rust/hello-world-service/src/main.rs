use log::info;
use std::collections::HashMap;
use actix_web::{get, web, App, HttpServer, HttpResponse, Responder, Result};
use serde::Serialize;

use actix_web_prom::{PrometheusMetrics, PrometheusMetricsBuilder};
async fn health() -> HttpResponse {
    HttpResponse::Ok().finish()
}

#[derive(Serialize)]
struct HelloWorldResponse {
    message: String,
}

#[get("/api/v1/hws")]
async fn hello() -> Result<impl Responder> {
    let obj = HelloWorldResponse {
        message: String::from("Hello from Rust"),
    };
    info!("Hi");
    Ok(web::Json(obj))
}

#[actix_web::main] // or #[tokio::main]
async fn main() -> std::io::Result<()> {
    env_logger::init();
    
    let mut labels = HashMap::new();
    labels.insert("label1".to_string(), "value1".to_string());
    let prometheus = PrometheusMetricsBuilder::new("api")
        .endpoint("/metrics")
        .const_labels(labels)
        .build()
        .unwrap();
    HttpServer::new(move || {
        App::new().
            wrap(prometheus.clone()).
            service(web::resource("/health").to(health)).
            service(hello)
    })
    // .bind(("127.0.0.1", 80))? // For local debugging with VS Code uncomment this line
    .bind(("0.0.0.0", 80))? // When building the docker image and running the container from it uncomment this line: listening on all available network interfaces or addresses on the machine
    .run()
    .await
}