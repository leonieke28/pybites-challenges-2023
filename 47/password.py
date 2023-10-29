import string

PUNCTUATION_CHARS = list(string.punctuation)

used_passwords = set("PassWord@1 PyBit$s9".split())


def validate_password(password):
    if (
        6 <= len(password) <= 12
        and any(char.isdigit() for char in password)
        and sum(char.islower() for char in password) >= 2
        and any(char.isupper() for char in password)
        and any(char in PUNCTUATION_CHARS for char in password)
        and password not in used_passwords
    ):
        used_passwords.add(password)
        return True
    return False
