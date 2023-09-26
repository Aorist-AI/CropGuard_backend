import secrets
import string
import random


def generate_code():
    alphabet = string.ascii_letters + string.digits
    while True:
        password = ''.join(secrets.choice(alphabet) for i in range(7))
        if (any(c.islower() for c in password) and any(c.isupper()
                                                       for c in password) and sum(c.isdigit() for c in password) >= 3):
            return password.upper()


def forgot_pass():
    alphabet = string.ascii_letters.upper() + string.digits
    while True:
        password = ''.join(secrets.choice(alphabet) for i in range(6))
        if (any(c.isupper()
                for c in password) and sum(c.isdigit() for c in password) >= 5):
            return password.upper()


def reset_post_code():
    alphabet = string.ascii_letters + string.digits
    while True:
        password = ''.join(secrets.choice(alphabet) for i in range(10))
        if (any(c.islower() for c in password) and any(c.isupper()
                                                       for c in password) and sum(c.isdigit() for c in password) >= 3):
            return password.upper()


def user_locator():
    alphabet = string.ascii_letters + string.digits
    while True:
        password = ''.join(secrets.choice(alphabet) for i in range(9))
        if (any(c.islower() for c in password) and any(c.isupper()
                                                       for c in password) and sum(c.isdigit() for c in password) >= 5):
            return password.upper()


def user_code():
    alphabet = string.ascii_letters + string.digits
    while True:
        password = ''.join(secrets.choice(alphabet) for i in range(11))
        if (any(c.islower() for c in password) and any(c.isupper()
                                                       for c in password) and sum(c.isdigit() for c in password) >= 8):
            return password.upper()

