import random
import string
import secrets


MAX_CHAR = 20
PASS_LENGTH = 30


def filler(length):
    x = ''.join(random.choices(string.ascii_letters + string.digits, k=(MAX_CHAR-length)))
    return x

def password():
    p = ''.join(secrets.choice(string.ascii_letters + string.digits) for i in range(PASS_LENGTH))
    return p
