import argparse
import re
import logging
import sys

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def setup_argparse():
    """
    Sets up argument parsing for the command-line interface.
    Returns:
        argparse.ArgumentParser: Configured argument parser.
    """
    parser = argparse.ArgumentParser(
        description="sm-Password-Strength-Checker: Evaluates the strength of passwords based on configurable criteria.",
        epilog="Example usage: python main.py --password MySecurePassword123!"
    )
    parser.add_argument(
        "--password",
        type=str,
        required=True,
        help="The password to evaluate for strength."
    )
    parser.add_argument(
        "--version",
        action="version",
        version="sm-Password-Strength-Checker 1.0",
        help="Show the tool's version information."
    )
    return parser

def check_password_strength(password):
    """
    Evaluates the strength of a password based on configurable criteria.
    Args:
        password (str): The password to check.
    Returns:
        str: Strength evaluation message.
    """
    if len(password) < 8:
        return "Weak: Password must be at least 8 characters long."
    if not re.search(r'[A-Z]', password):
        return "Weak: Password must contain at least one uppercase letter."
    if not re.search(r'[a-z]', password):
        return "Weak: Password must contain at least one lowercase letter."
    if not re.search(r'[0-9]', password):
        return "Weak: Password must contain at least one digit."
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "Weak: Password must contain at least one special character."
    return "Strong: Your password meets the criteria."

def main():
    """
    Main function that parses arguments and evaluates password strength.
    """
    try:
        parser = setup_argparse()
        args = parser.parse_args()

        password = args.password
        logging.info("Evaluating password strength...")
        result = check_password_strength(password)
        logging.info("Password strength evaluation completed.")
        print(result)

    except Exception as e:
        logging.error(f"An error occurred: {e}", exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    main()