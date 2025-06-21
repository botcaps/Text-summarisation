# Import standard and third-party libraries for file operations, configuration management, and logging
import os                              # Helps with file system operations like creating directories and checking file sizes
from box.exceptions import BoxValueError  # Custom exception for handling issues specific to Box library
import yaml                            # Library to read and parse YAML configuration files
from text_summarizer.logging import logger  # Custom logger to record process and errors throughout the project
from ensure import ensure_annotations  # Ensures that function type annotations are respected at runtime
from box import ConfigBox              # Enhanced dictionary that allows dot notation access for configuration
from pathlib import Path               # Provides an object-oriented way to handle file paths
from typing import Any                 # For general-purpose type hinting (used for flexibility in function signatures)


@ensure_annotations  # Ensures function inputs and outputs match the type hints
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns its contents as a ConfigBox object
    to allow dot notation access to configuration parameters.
    """
    try:
        # Open and safely load the YAML file into a Python dictionary
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            
            # Wrap the dictionary with ConfigBox for dot-access
            return ConfigBox(content)
    
    # Specific error if the YAML file is empty or malformed for Box
    except BoxValueError as e:
        raise ValueError("yaml file is empty")
    
    # Catch any other unexpected exceptions
    except Exception as e:
        raise e

@ensure_annotations  # Ensures type correctness for function inputs
def create_directories(path_to_directories: list, verbose=True):
    """
    Creates all directories provided in the list.
    If 'verbose' is True, logs every directory creation.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)  # Safely creates the directory if it doesn't exist (avoids errors)
        
        if verbose:
            logger.info(f"created directory at: {path}")  # Logs the directory creation if verbosity is enabled


@ensure_annotations  # Enforce type annotations at runtime
def get_size(path: Path) -> str:
    """
    Returns the size of the specified file in kilobytes (KB).
    """
    size = round(os.path.getsize(path) / 1024)  # Get file size in bytes and convert to KB
    return f"{size} KB"                         # Return the size as a string with unit label
