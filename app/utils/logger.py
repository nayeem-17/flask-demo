import logging
import os
from logging.handlers import RotatingFileHandler
from flask import has_request_context, request


class RequestFormatter(logging.Formatter):
    def format(self, record):
        if has_request_context():
            record.url = request.url
            record.remote_addr = request.remote_addr
        else:
            record.url = None
            record.remote_addr = None

        return super().format(record)


def setup_logger(app):
    # Create logs directory if it doesn't exist
    if not os.path.exists("logs"):
        os.mkdir("logs")

    # Set up file handler
    file_handler = RotatingFileHandler("logs/app.log", maxBytes=10240, backupCount=10)
    file_handler.setFormatter(
        RequestFormatter(
            "[%(asctime)s] %(remote_addr)s requested %(url)s\n"
            "%(levelname)s in %(module)s: %(message)s"
        )
    )
    file_handler.setLevel(logging.INFO)

    # Set up console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(
        logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    )
    console_handler.setLevel(logging.DEBUG)

    # Get the logger
    logger = logging.getLogger(app.import_name)
    logger.setLevel(logging.DEBUG)

    # Add handlers
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


# Usage in other files
logger = logging.getLogger("your_app_name")
