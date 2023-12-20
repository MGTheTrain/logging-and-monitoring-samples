use log::info;
use actix_web::{get, web, App, HttpServer, HttpResponse, Responder, Result};
use serde::Serialize;

use log;
use loki_logger;
use log::LevelFilter;

use std::env;
use chrono::Utc;

#[derive(Serialize)]
struct HelloWorldResponse {
    message: String,
}

#[get("/api/v1/hws")]
async fn hello() -> Result<impl Responder> {
    let obj = HelloWorldResponse {
        message: String::from("Hello from Rust"),
    };
    // Get the current UTC time
    let timestamp = Utc::now().to_rfc3339();
    log::info!("{}: Hello from Rust", timestamp);
    Ok(web::Json(obj))
}

#[actix_web::main] // or #[tokio::main]
async fn main() -> std::io::Result<()> {
    // Get the Loki URL from an environment variable or use a default value
    let loki_url = match env::var("LOKI_URL") {
        Ok(url) => url,
        Err(_) => String::from("http://192.168.99.100:3100/loki/api/v1/push"), // Default URL
    };

    loki_logger::init(&loki_url, log::LevelFilter::Info).unwrap();

    HttpServer::new(move || {
        App::new().service(hello)
    })
    .bind(("0.0.0.0", 80))? // Listening on all available network interfaces or addresses on the machine
    .run()
    .await
}
