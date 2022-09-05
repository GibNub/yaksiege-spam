import random
import string
import secrets


def filler(length):
    x = ''.join(random.choices(string.ascii_letters + string.digits, k=(20-length)))
    return x

def password():
    p = ''.join(secrets.choice(string.ascii_letters + string.digits) for i in range(30))
    return p
