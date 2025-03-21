import json
import os
from cli_tool.logger import setup_logger

# Initialize logger
logger = setup_logger()

CONFIG_FILE = "config.json"

def load_config():
    """
    Loads configuration settings from a JSON file.
    
    Returns:
    - dict: Configuration settings.
    """
    if not os.path.exists(CONFIG_FILE):
        logger.warning("Config file not found. Creating default config.json.")
        save_config({})  # Create an empty config file
    
    try:
        with open(CONFIG_FILE, "r") as file:
            config = json.load(file)
            logger.info("Configuration loaded successfully.")
            return config
    except json.JSONDecodeError:
        logger.error("Error decoding config file. Resetting to default.")
        save_config({})
        return {}

def save_config(config_data):
    """
    Saves configuration settings to a JSON file.

    Parameters:
    - config_data (dict): Configuration settings to save.
    """
    with open(CONFIG_FILE, "w") as file:
        json.dump(config_data, file, indent=4)
        logger.info("Configuration updated successfully.")

def set_config(key, value):
    """
    Updates a configuration setting.
    
    Parameters:
    - key (str): The configuration key.
    - value (str): The value to set.
    """
    config = load_config()
    config[key] = value
    save_config(config)
    logger.info(f"Config updated: {key} = {value}")

def get_config(key):
    """
    Retrieves a configuration value.

    Parameters:
    - key (str): The configuration key.

    Returns:
    - str: The value of the configuration key or None if not found.
    """
    config = load_config()
    return config.get(key, None)
