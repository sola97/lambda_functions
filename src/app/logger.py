import logging.config
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
log_path = os.path.join(current_dir, '..', 'logging_config.ini')

logging.config.fileConfig(log_path)
logger = logging.getLogger("my_logger")
