# Import necessary libraries
import os                         # For creating directories and working with the file system
from pathlib import Path           # For handling file paths in a clean, cross-platform way
import logging                     # For logging the process of file and directory creation

# Configure logging: INFO level, and a readable log message format
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Define the project name (used as the base package folder)
project_name = "text_summarizer"

# List of all the files and folders you want to create for your project structure
list_of_files = [
    ".github/workflows/.gitkeep",                        # For GitHub Actions CI/CD workflows
    f"src/{project_name}/__init__.py",                   # Makes the folder a Python package
    f"src/{project_name}/components/__init__.py",        # Components folder (could be data loader, model, etc.)
    f"src/{project_name}/utils/__init__.py",             # Utilities folder
    f"src/{project_name}/utils/common.py",               # Common helper functions
    f"src/{project_name}/logging/__init__.py",           # Logging module folder
    f"src/{project_name}/config/__init__.py",            # Configuration module
    f"src/{project_name}/config/configuration.py",       # File to manage configuration loading
    f"src/{project_name}/pipeline/__init__.py",          # Pipeline folder (for training, prediction, etc.)
    f"src/{project_name}/entity/__init__.py",            # Entity folder (data classes / schemas)
    f"src/{project_name}/constants/__init__.py",         # Constants folder (hyperparameters, file paths, etc.)
    "config/config.yaml",                                # External configuration file
    "params.yaml",                                       # Model and pipeline parameters
    "app.py",                                            # Entry point for the Streamlit or Flask app
    "main.py",                                           # Project orchestrator (could trigger training, prediction)
    "Dockerfile",                                        # For containerizing the project
    "requirements.txt",                                  # Python dependencies list
    "setup.py",                                          # Package installation script
    "research/trials.ipynb",                             # Jupyter notebook for experiments and prototyping
]   

# Loop through each file path and create files/folders if they don't already exist
for filepath in list_of_files:
    filepath = Path(filepath)                         # Convert string to Path object for cross-platform support
    filedir, filename = os.path.split(filepath)       # Separate directory path and filename

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)           # Create the directory if it doesn't exist
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    # Create the file if it doesn't exist or if it exists but is empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass                                      # Create an empty file (no content yet)
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"File already exists: {filepath}")  # Skip creating the file if it already exists with content
