"""
WEEK 16
Exercise 2: General dictionary attacks

"""

import requests
import hashlib

# Download the phpbb password list
url = "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Leaked-Databases/phpbb.txt"
response = requests.get(url)
passwords = response.text.splitlines()

# enter the given hash
given_hash = "3ddcd95d2bff8e97d3ad817f718ae207b98c7f2c84c5519f89cd15d7f8ee1c3b"

# Function to apply hash
def apply_hash(password, hash_function):
    return hash_function(password.encode()).hexdigest()

# Function to perform the dictionary attack
def dictionary_attack(given_hash, passwords):
    hash_functions = [hashlib.sha256, hashlib.sha512, hashlib.sha1]  # Add more if needed

    for hash_function in hash_functions:
        for password in passwords:
            hashed_password = apply_hash(password, hash_function)
            if hashed_password == given_hash:
                return f"Password: {password}, Hash Function: {hash_function.__name__}"

    return "Password not found in the phpbb dictionary."

# Run the attack and print the result
result = dictionary_attack(given_hash, passwords)
print(result)

