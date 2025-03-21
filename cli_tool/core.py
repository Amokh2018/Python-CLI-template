import time
from cli_tool.logger import setup_logger

# Initialize logger
logger = setup_logger()

def perform_operation(input_value: str) -> str:
    """
    Simulates an operation performed by the CLI tool.

    Parameters:
    - input_value (str): The user input provided via the CLI.

    Returns:
    - str: A message confirming the operation.
    """
    logger.info(f"Operation started with input: {input_value}")

    # Simulate processing time
    time.sleep(1)

    if not input_value.strip():
        logger.error("Invalid input: Empty string received.")
        raise ValueError("Input cannot be empty.")

    result = f"Processed input: {input_value.upper()}"
    
    logger.info(f"Operation completed successfully. Result: {result}")
    
    return result
