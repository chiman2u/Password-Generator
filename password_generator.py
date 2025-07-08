import string
import random

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
    print("Generated Password:", generate_password(16))
