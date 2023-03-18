import string
import random

characters = list(string.ascii_letters + string.digits + '!@#$%^&*()')

def generate_password():
    password_length = int(input("HOw long you want your password should be?"))
    random.shuffle(characters)

    password = []

    for x in range(password_length):
        password.append(random.choice(characters))

        random.shuffle(password)

        password = "".join(password)

        print(password)

