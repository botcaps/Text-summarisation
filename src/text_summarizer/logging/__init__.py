# Import required libraries
import logging      # Built-in Python module for logging events, errors, and messages
import os           # For interacting with the file system (like creating folders)
from datetime import datetime  # For working with timestamps (not directly used here, but commonly helpful)
import sys          # To direct logs to the console output (stdout)

# Define the log message format
# Example format: [2025-06-21 11:05:00,123: INFO: module_name: This is a log message.]
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Define the directory where log files will be stored
log_dir = "logs"

# Define the complete log file path (logs/running_logs.log)
log_filepath = os.path.join(log_dir, "running_logs.log")

# Create the log directory if it doesn't already exist
os.makedirs(log_dir, exist_ok=True)

# Configure the logging settings
logging.basicConfig(
    level=logging.INFO,        # Set the logging level to INFO (you can also use DEBUG, WARNING, ERROR, etc.)
    format=logging_str,        # Apply the custom log format defined above
    handlers=[
        logging.FileHandler(log_filepath),    # Write logs to the file at log_filepath
        logging.StreamHandler(sys.stdout)     # Also print logs to the console in real-time
    ]
)

# Create a logger instance with a custom name (use this in your project to log messages)
logger = logging.getLogger("textSummarizerLogger")
