"""
WEEK 16
Exercise 3-A: Personalised dictionary attack 

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
    base_passwords = []
    for key, value in info.items():
        if 'birthday' in key:
            base_passwords.extend(format_date(value))
        else:
            base_passwords.append(value)
    
    # Combine different pieces of information
    combined_passwords = []
    for combo in itertools.combinations(base_passwords, 2):
        combined_passwords.append(''.join(combo))
        combined_passwords.append(''.join(combo[::-1]))  # reverse combination

    return base_passwords + combined_passwords

# Hash function with salt
def hash_with_salt(password, salt):
    return hashlib.sha256((password + salt).encode()).hexdigest()

# Given hash and salt
given_hash = "3281e6de7fa3c6fd6d6c8098347aeb06bd35b0f74b96f173c7b2d28135e14d45"
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
