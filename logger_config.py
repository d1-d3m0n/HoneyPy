import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name, log_file, level=logging.INFO):
    # Sets up a rotating logger.
    formatter = logging.Formatter('[%(asctime)s] [%(name)s] %(message)s', "%Y-%m-%d %H:%M:%S")
    handler = RotatingFileHandler(log_file, maxBytes=5*1024, backupCount=3)
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    logger.propagate = False
    return logger

# Create log directory if it doesn't exist
if not os.path.exists("logs"):
    os.makedirs("logs")

# Define loggers
ssh_logger = setup_logger("SSH", "logs/ssh_activity.log")
http_logger = setup_logger("HTTP", "logs/http_activity.log")
error_logger = setup_logger("ERROR", "logs/honeypot_errors.log")
