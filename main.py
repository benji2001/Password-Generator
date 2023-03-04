import random
import string

def generate_password(length=12):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    while True:
        password = ''.join(random.choice(alphabet) for i in range(length))
        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and any(c.isdigit() for c in password)
                and any(c in string.punctuation for c in password)):
            break
    return password

if __name__ == '__main__':
    password = generate_password()
    print(f"Your new password is: {password}")
