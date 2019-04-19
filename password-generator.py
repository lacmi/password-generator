import secrets
import string
import pyperclip

alphanumeric = string.ascii_letters + string.digits
allCharacters = alphanumeric + string.punctuation
length = 20

while True:
    password = ''.join(secrets.choice(allCharacters) for x in range(length))
    if(any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and any(c.isdigit() for c in password)
            and any(c in string.punctuation for c in password)):
        break

pyperclip.copy(password)
