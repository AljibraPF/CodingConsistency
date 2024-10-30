import random
import string

#Code that generates a random password!

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

print("Generated Password:", generate_password(12))
