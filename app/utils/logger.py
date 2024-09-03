import logging
import os
from datetime import datetime

# Get the current date to create the log directory
current_date = datetime.now().strftime("%Y-%m-%d")
log_directory = f"logs/{current_date}"

# Create the log directory if it doesn't exist
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

# Create separate handlers for different log levels
debug_handler = logging.FileHandler(os.path.join(log_directory, "debug.log"))
debug_handler.setLevel(logging.DEBUG)
debug_handler.addFilter(lambda record: record.levelno == logging.DEBUG)

info_handler = logging.FileHandler(os.path.join(log_directory, "info.log"))
info_handler.setLevel(logging.INFO)
info_handler.addFilter(lambda record: record.levelno == logging.INFO)

error_handler = logging.FileHandler(os.path.join(log_directory, "error.log"))
error_handler.setLevel(logging.ERROR)
error_handler.addFilter(lambda record: record.levelno >= logging.ERROR)

# Create a handler for all logs in app.log
app_handler = logging.FileHandler(os.path.join(log_directory, "app.log"))
app_handler.setLevel(logging.DEBUG)  # Capture all logs

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)  # Log all levels to the console

# Create formatters and add them to handlers
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
debug_handler.setFormatter(formatter)
info_handler.setFormatter(formatter)
error_handler.setFormatter(formatter)
app_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Get the root logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)  # Set the lowest level to capture all logs

# Clear existing handlers to avoid duplicate logs
if logger.hasHandlers():
    logger.handlers.clear()

# Add handlers to the logger
logger.addHandler(debug_handler)
logger.addHandler(info_handler)
logger.addHandler(error_handler)
logger.addHandler(app_handler)
logger.addHandler(console_handler)

# Suppress werkzeug logs except for errors
werkzeug_logger = logging.getLogger("werkzeug")
werkzeug_logger.setLevel(logging.ERROR)

# Suppress geventwebsocket.handler debug logs
geventwebsocket_logger = logging.getLogger("geventwebsocket.handler")
geventwebsocket_logger.setLevel(
    logging.INFO
)  # Set to INFO or ERROR to suppress DEBUG logs

# Create a custom logger
app_logger = logging.getLogger(__name__)


# Custom filter to exclude static file logs
class StaticFileFilter(logging.Filter):
    def filter(self, record):
        # Exclude logs related to static files
        return not any(
            static_path in record.getMessage()
            for static_path in ["/static/", "/favicon.ico"]
        )


# Apply the filter to the geventwebsocket logger
geventwebsocket_logger.addFilter(StaticFileFilter())

# Apply the filter to all handlers if necessary
for handler in logger.handlers:
    handler.addFilter(StaticFileFilter())
