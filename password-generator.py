import secrets
import string
import argparse
import pyperclip


alphanumeric = string.ascii_letters + string.digits
allCharacters = alphanumeric + string.punctuation
default_length = 20


def generate_password(length):
    while True:
        password = ''.join(secrets.choice(allCharacters) for x in range(length))
        if(any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and any(c.isdigit() for c in password)
                and any(c in string.punctuation for c in password)):
            break
    return password

def positive(length):
    try:
        i = int(length)
    except ValueError:
        raise argparse.ArgumentTypeError("length must be an integer")
    if i < 1:
        raise argparse.ArgumentTypeError("length must be at least 1")
    return i


parser = argparse.ArgumentParser(description="password generator")
parser.add_argument("-l", "--length", type=positive, default=default_length, help="specify the length of the password")


if __name__ == "__main__":
    args = parser.parse_args()
    password = generate_password(args.length)
    pyperclip.copy(password)
