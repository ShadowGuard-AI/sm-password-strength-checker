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
        "-p", "--password",
        type=str,
        required=True,
        help="The password to evaluate for strength."
    )
    parser.add_argument(
        "-l", "--min-length",
        type=int,
        default=8,
        help="Minimum password length (default: 8)."
    )
    parser.add_argument(
        "-u", "--min-uppercase",
        type=int,
        default=1,
        help="Minimum number of uppercase characters (default: 1)."
    )
    parser.add_argument(
        "-d", "--min-digits",
        type=int,
        default=1,
        help="Minimum number of digits (default: 1)."
    )
    parser.add_argument(
        "-s", "--min-special",
        type=int,
        default=1,
        help="Minimum number of special characters (default: 1)."
    )
    parser.add_argument(
        "--version",
        action="version",
        version="sm-Password-Strength-Checker 1.0",
        help="Show the tool's version information."
    )
    return parser

def check_password_strength(password, min_length=8, min_uppercase=1,
                            min_digits=1, min_special=1):
    """
    Evaluates the strength of a password based on configurable criteria.
    At least one lowercase letter is always required, as in the original
    fixed criteria. Only the first failing criterion is reported.
    Args:
        password (str): The password to check.
        min_length (int): Minimum number of characters.
        min_uppercase (int): Minimum number of uppercase letters.
        min_digits (int): Minimum number of digits.
        min_special (int): Minimum number of special characters.
    Returns:
        str: Strength evaluation message.
    """
    if len(password) < min_length:
        return f"Weak: Password must be at least {min_length} characters long."
    # My classes are ASCII ranges only. A capital letter outside A to Z, or a digit from
    # another script, earns no credit here even though the person typing it did what was asked.
    if len(re.findall(r'[A-Z]', password)) < min_uppercase:
        if min_uppercase == 1:
            return "Weak: Password must contain at least one uppercase letter."
        return f"Weak: Password must contain at least {min_uppercase} uppercase letters."
    if not re.search(r'[a-z]', password):
        return "Weak: Password must contain at least one lowercase letter."
    if len(re.findall(r'[0-9]', password)) < min_digits:
        if min_digits == 1:
            return "Weak: Password must contain at least one digit."
        return f"Weak: Password must contain at least {min_digits} digits."
    # The special set is this fixed list. A dash, an underscore, a plus sign, a bracket, or a
    # space in the password earns no special credit from me.
    if len(re.findall(r'[!@#$%^&*(),.?":{}|<>]', password)) < min_special:
        if min_special == 1:
            return "Weak: Password must contain at least one special character."
        return f"Weak: Password must contain at least {min_special} special characters."
    return "Strong: Your password meets the criteria."

def main():
    """
    Main function that parses arguments and evaluates password strength.
    """
    try:
        parser = setup_argparse()
        args = parser.parse_args()

        if args.min_length < 1 or args.min_uppercase < 0 or args.min_digits < 0 or args.min_special < 0:
            parser.error("minimum length must be at least 1 and other minimums must be 0 or more")

        password = args.password
        logging.info("Evaluating password strength...")
        # The password arrives as a command line argument, which puts it in shell history and in
        # the process list while I run. That trade suits a quick check and not a password that
        # matters, and the Weak verdict below still exits 0, so only the printed word carries it.
        result = check_password_strength(
            password,
            min_length=args.min_length,
            min_uppercase=args.min_uppercase,
            min_digits=args.min_digits,
            min_special=args.min_special
        )
        logging.info("Password strength evaluation completed.")
        print(result)

    except Exception as e:
        logging.error(f"An error occurred: {e}", exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    main()