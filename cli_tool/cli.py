import argparse
import sys
from cli_tool.core import perform_operation
from cli_tool.logger import setup_logger

# Initialize logger
logger = setup_logger()

def main():
    """
    Main function to handle CLI arguments.
    """
    parser = argparse.ArgumentParser(
        description="CLI Tool Template - A starter CLI for building Python applications."
    )
    
    # Add a subparser to handle multiple commands
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Command: run
    run_parser = subparsers.add_parser("run", help="Execute the main operation.")
    run_parser.add_argument("input", type=str, help="Input value for the operation.")

    # Command: config
    config_parser = subparsers.add_parser("config", help="Set a configuration value.")
    config_parser.add_argument("--set", type=str, help="Set a new config value.")

    # Command: version
    subparsers.add_parser("version", help="Show the CLI version.")

    args = parser.parse_args()

    # Handle commands
    if args.command == "run":
        try:
            result = perform_operation(args.input)
            print(f"Result: {result}")
        except Exception as e:
            logger.error(f"Error: {e}")
            print("An error occurred. Check logs for details.")
    
    elif args.command == "config":
        if args.set:
            print(f"Configuration set to: {args.set}")
            logger.info(f"Configuration updated: {args.set}")
        else:
            print("No configuration value provided.")
    
    elif args.command == "version":
        print("CLI Tool v1.0.0")
    
    else:
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()
