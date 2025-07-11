import argparse
import string
import random
import sys

import pyperclip

def generate_password(length = 10, upper = True, lower = True, digits = True, symbol = True): #Default values
    """
    Generate a random password based on the selected character types.

    Args:
        length (int): Length of the password.
        upper (bool): Include uppercase letters.
        lower (bool): Include lowercase letters.
        digits (bool): Include digits.
        symbol (bool): Include symbols.

    Returns:
        str: Generated password.

    Raises:
        ValueError: If no character types are selected.
    """
    if length < 1:
        raise ValueError("Password length must be at least 1.")
    
    characters = ""
    if upper:
        characters += string.ascii_uppercase
    if lower:
        characters += string.ascii_lowercase
    if digits:
        characters += string.digits
    if symbol:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character type must be selected")
    
    password = "".join(random.choice(characters) for _ in range(length))

    return password


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a secure random password.") #Arguments to that can be inputted into the CLI
    parser.add_argument("-l", "--length", type=int, default=10, help="Length of the password (default: 10)")
    parser.add_argument("--no-upper", action="store_true", help="Exclude uppercase letters")
    parser.add_argument("--no-lower", action="store_true", help="Exclude lowercase letters")
    parser.add_argument("--no-digits", action="store_true", help="Exclude digits")
    parser.add_argument("--no-symbols", action="store_true", help="Exclude symbols")
    parser.add_argument("--copy", action="store_true", help="Copy password to clipboard")

    if len(sys.argv) == 1: #If no argument is passed into the command line start interactive generator
        print("Interactive Password Generator")
        try:
            length = int(input("Password length (e.g. 12): "))
            upper = input("Include UPPERCASE letters? (y/n): ").lower().startswith("y")
            lower = input("Include lowercase letters? (y/n): ").lower().startswith("y")
            digits = input("Include digits? (y/n): ").lower().startswith("y")
            symbols = input("Include symbols? (y/n): ").lower().startswith("y")
            copy = input("Copy to clipboard? (y/n): ").lower().startswith("y")

            password = generate_password(length, upper, lower, digits, symbols)
            print("Generated Password:", password)

            if copy:
                pyperclip.copy(password)
                print("Password copied to clipboard!")

        except ValueError as e:
            print("Error:", e)
    else:

        args = parser.parse_args()

        try:
            password = generate_password(
                length=args.length,
                upper=not args.no_upper,
                lower=not args.no_lower,
                digits=not args.no_digits,
             symbol=not args.no_symbols
            )

            print("Generated Password:", password)
            if args.copy:
                pyperclip.copy(password)
                print ("Password Copied to clipboard!")

        except ValueError as e:
            print("Error:", e)
