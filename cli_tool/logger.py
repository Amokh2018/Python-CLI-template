import logging
import os

def setup_logger(log_file="cli_tool.log"):
    """
    Configures and returns a logger for the CLI tool.

    Parameters:
    - log_file (str): The file where logs will be stored.

    Returns:
    - logging.Logger: Configured logger instance.
    """
    log_directory = "logs"
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)  # Ensure logs folder exists
    
    log_file_path = os.path.join(log_directory, log_file)

    # Create a logger
    logger = logging.getLogger("CLI_Tool")
    logger.setLevel(logging.DEBUG)

    # Create file handler to write logs to a file
    file_handler = logging.FileHandler(log_file_path)
    file_handler.setLevel(logging.DEBUG)

    # Create console handler to display logs on the console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Define log format
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
