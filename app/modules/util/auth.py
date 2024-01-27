"""

Utility methods for authentication.
----------------

"""
from app.models import Users
from re import fullmatch


def check_if_user_already_exists(email: str) -> bool:
    """
    Checks if a user with the given email already exists.

    :param email: email to check
    :return: True if the user exists, False otherwise
    """
    return Users.query.filter_by(email=email).first() is not None


def check_password_confirmation(
    password: str, password_confirmation: str
) -> bool:
    """
    Checks if the password and password confirmation are the same.

    :param password: password
    :param password_confirmation: password confirmation to check against
    :return: True if the passwords are the same, False otherwise
    """
    return password == password_confirmation


def check_password_strength(password: str) -> bool:
    """
    Checks the strength of a password.

    Will pass if the given password is at least 8 characters long, has no
    repeating characters, and has at least one uppercase letter.

    :param password: password to check
    :return: True if the password is strong, False otherwise
    """
    return (
        len(password) >= 8
        and not fullmatch(r"(.)\1*", password)
        and not fullmatch(r"[a-z]*", password)
    )
