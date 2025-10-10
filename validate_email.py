import re
from typing import List

def validate_email(email: str) -> bool:
    """
    Validate the given email address using a regular expression.

    Args:
        email (str): The email address to validate.

    Returns:
        bool: True if the email address is valid, False otherwise.
    """
    # Regular expression pattern for validating an email address
    pattern = re.compile(
        r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    )
    
    return bool(pattern.match(email))

def validate_email_list(emails: List[str]) -> List[str]:
    """
    Validate a list of email addresses and return the list of invalid emails.

    Args:
        emails (List[str]): The list of email addresses to validate.

    Returns:
        List[str]: A list containing invalid email addresses.
    """
    return [email for email in emails if not validate_email(email)]

def main():
    """
    Main function to validate a list of email addresses and handle errors.
    """
    emails = [
        "test@example.com",
        "invalid-email",
        "another.test@domain.co",
        "no-at-symbol.com",
        "special+chars@domain.com"
    ]

    invalid_emails = validate_email_list(emails)

    if invalid_emails:
        print("The following email addresses are invalid:")
        for email in invalid_emails:
            print(f" - {email}")
    else:
        print("All email addresses are valid.")

if __name__ == "__main__":
    main()