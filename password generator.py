import random
import string

uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase
numbers = string.digits
symbols = string.punctuation

all_characters = uppercase + lowercase + numbers + symbols

length = int(input("Enter password length: "))

if length < 4:
    print("Password length must be at least 4")

else:
    password = ""

    # Add mandatory characters
    password += random.choice(uppercase)
    password += random.choice(lowercase)
    password += random.choice(numbers)
    password += random.choice(symbols)

    # Add remaining characters
    for ch in range(length -4):
        password += random.choice(all_characters)

    # Convert string to list for shuffling
    password = list(password)

    # Shuffle characters
    random.shuffle(password)

    # Convert list back to string
    password = "".join(password)

    print("Generated password:", password)