#!/usr/bin/python3

import re
from typing import Dict
from email.message import EmailMessage


def validate_name(name: str, name_type: str) -> str:
    """
    Validates sender and receiver name based on their
    name_type (sender/receiver) and returns the name.
    Raises ValueError if validation fails.
    """
    name = name.strip()
    if not ((
            5 <= len(name) <= 30) if name_type == 'sender' else (
            5 <= len(name) <= 60)):
        raise ValueError(f"{name_type.capitalize()} name should be between 5 to 30 characters long" if name_type ==
                         'sender' else f"{name_type.capitalize()} name should be between 5 to 60 characters long")
    return name


def validate_email_addr(email_addr: str) -> bool:
    """
    Returns True if email address is valid. Otherwise, returns False.
    """
    # Total length of email too long.
    if len(email_addr) > 254:
        return False

    # No domain!
    if email_addr.count('@') != 1:
        return False

    # Email address pattern regex
    pattern = re.compile(
        r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)*(\.[a-zA-Z]{2,4})$')

    if not pattern.match(email_addr):
        return False

    return True


def validate_html_replacements(
        html: str, replacements: Dict[str, str]) -> None:
    """
    Validates html and replacements and raises ValueError if html or replacements are invalid.
    """
    if not replacements:
        raise ValueError("Replacements dictionary is empty.")

    pattern = re.compile(r'\((.*?)\)')

    # Validate replacements
    for match in pattern.findall(html):
        if match not in replacements:
            raise ValueError(
                f"Replacement key '{match}' not found in the replacements dictionary.")

    for key in replacements:
        if f"({key})" not in html:
            raise ValueError(f"Replacement key '{key}' not found in the HTML.")


def validate_email_payload(
        sender_name: str,
        sender_addr: str,
        receiver_name: str,
        receiver_addr: str,
        html: str,
        replacements: Dict[str, str]) -> bool:
    try:
        # Check that all required keys are present in the replacements dictionary
        required_keys = {
            "<receiver_name>",
            "<sender_name>",
            "<receiver_addr>",
            "<sender_addr>"}
        if not required_keys.issubset(set(replacements.keys())):
            return False

        # Replace the placeholders in the HTML string with their corresponding values
        for placeholder, value in replacements.items():
            html = html.replace(placeholder, value)

        # Validate the sender and receiver names
        validate_name(sender_name, 'sender')
        validate_name(receiver_name, 'receiver')

        # Validate the sender and receiver addresses
        if not validate_email_addr(sender_addr) or not validate_email_addr(receiver_addr):
            return False

        # Build the email message and validate it
        msg = EmailMessage()
        msg.set_content(html, subtype="html")
        msg["From"] = f"{sender_name} <{sender_addr}>"
        msg["To"] = f"{receiver_name} <{receiver_addr}>"
        msg["Subject"] = "Test Email Subject"
        msg.as_string()

    except Exception:
        return False

    return True
