import logging
import logging_loki

def configure_logger(logger, loki_url):
    logger.setLevel(logging.DEBUG)
    # Create a LokiHandler and set its URL
    loki_handler = logging_loki.LokiHandler(
        url=loki_url,
        tags={"application": "python-hello-world-service"},
        version="1",
    )
    # Add the LokiHandler to the logger
    logger.addHandler(loki_handler)
