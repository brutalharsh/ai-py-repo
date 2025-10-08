import re

def validate_email(email: str) -> bool:
    """
    Validate the given email address.

    Args:
        email (str): The email address to validate.

    Returns:
        bool: True if the email address is valid, False otherwise.

    Raises:
        ValueError: If the email address is invalid.
    """
    # Regular expression pattern for validating an email address
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
    if re.match(pattern, email):
        return True
    else:
        raise ValueError(f"Invalid email address: {email}")

if __name__ == "__main__":
    # Example usage
    emails = [
        "test@example.com",
        "invalid-email",
        "another.test@domain.co",
        "no-at-symbol.com",
        "special+chars@domain.com"
    ]

    for email in emails:
        try:
            print(f"Validating {email}: {validate_email(email)}")
        except ValueError as e:
            print(e)