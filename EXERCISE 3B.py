"""
WEEK 16
Exercise 3-B: Personalised dictionary attack 

"""

import hashlib
import itertools

# Personal information
user_info = {
    "username": "laplusbelle",
    "name": "Marie",
    "surname": "Curie",
    "pet": "Woof",
    "birthday": "2 January, 1980",
    "employer": "UKC",
    "mother": "Jean Neoskour",
    "father": "Jvaist Fairecourir",
    "husband": "Eltrofor",
    "husband_birthday": "29 December, 1981"
}

# Function to format date in different ways
def format_date(date_str):
    formats = []
    day, month, year = date_str.split()
    formats.append(day + month + year)
    formats.append(year + month + day)
    formats.append(day + month[:3] + year)
    formats.append(year + month[:3] + day)
    return formats

# Generate potential passwords based on personal information
def generate_passwords(info):
    passwords = []
    for key, value in info.items():
        if 'birthday' in key:
            passwords.extend(format_date(value))
        else:
            passwords.append(value)
    return passwords

# Hash function with salt
def hash_with_salt(password, salt):
    return hashlib.sha256((password + salt).encode()).hexdigest()

# Given hash and salt
given_hash = "fc2298f491eac4cff95e7568806e088a901c904cda7dd3221f551e5b89b3c3aa"
salt = "5UA@/Mw^%He]SBaU"

# Generate passwords and perform the attack
potential_passwords = generate_passwords(user_info)
for password in potential_passwords:
    hashed_password = hash_with_salt(password, salt)
    if hashed_password == given_hash:
        print(f"Password found: {password}")
        break
else:
    print("Password not found in personalized dictionary.")
