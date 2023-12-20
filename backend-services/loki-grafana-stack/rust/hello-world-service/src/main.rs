use log::info;
use actix_web::{get, web, App, HttpServer, HttpResponse, Responder, Result};
use serde::Serialize;

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
    HttpServer::new(move || {
        App::new().
            service(hello)
    })
    .bind(("0.0.0.0", 80))? // Listening on all available network interfaces or addresses on the machine
    .run()
    .await
}