from random import randint


def generate_code():
    code = randint(100000, 999999)
    return str(code)
