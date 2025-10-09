import re

def validate_email(email: str) -> bool:
    """
    Validate the given email address.

    Args:
        email (str): The email address to validate.

    Returns:
        bool: True if the email address is valid, False otherwise.
    """
    # Regular expression pattern for validating an email address
    pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    
    return bool(pattern.match(email))

def main():
    """
    Main function to validate a list of email addresses.
    """
    emails = [
        "test@example.com",
        "invalid-email",
        "another.test@domain.co",
        "no-at-symbol.com",
        "special+chars@domain.com"
    ]

    for email in emails:
        try:
            if validate_email(email):
                print(f"Validating {email}: Valid")
            else:
                raise ValueError(f"Invalid email address: {email}")
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()