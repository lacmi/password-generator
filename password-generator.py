import secrets
import string
import argparse
import pyperclip


default_length = 20


def generate_password(length, spl_chars):
    characters = string.ascii_letters + string.digits
    if spl_chars:
        characters += string.punctuation
    while True:
        password = ''.join(secrets.choice(characters) for x in range(length))
        if (any(c.islower() for c in password) and any(c.isupper() for c in password) and any(c.isdigit() for c in password)):
            if spl_chars:
                if (any(c in string.punctuation for c in password)):
                    break
            else:
                break
    return password

def fourplus(length):
    try:
        i = int(length)
    except ValueError:
        raise argparse.ArgumentTypeError("length must be an integer")
    if i < 4:
        raise argparse.ArgumentTypeError("length must be at least 4")
    return i


parser = argparse.ArgumentParser(description="password generator")
parser.add_argument("-l", "--length", type=fourplus, default=default_length, help="specify the length of the password")
parser.add_argument("-a", "--alphanumeric", action="store_false", help="only alphanumeric characters")
parser.add_argument("-p", "--print", action="store_true", help="print the password instead of copying it to the clipboard")


if __name__ == "__main__":
    args = parser.parse_args()
    password = generate_password(args.length, args.alphanumeric)
    if args.print:
        print(password)
    else:
        pyperclip.copy(password)
