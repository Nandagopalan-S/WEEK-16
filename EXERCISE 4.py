"""
WEEK 16
Exercise 4: Breaking a graphical password (an Android unlock pattern) 

"""

import hashlib
import itertools
import time

# Function to hash a pattern
def hash_pattern(pattern):
    return hashlib.sha1(pattern.encode()).hexdigest()

# Function to generate all patterns
def generate_patterns():
    grid = 'abcdefghi'  # Grid labels corresponding to 0-8
    for length in range(1, 10):  # Patterns can be from 1 to 9 in length
        for pattern in itertools.permutations(grid, length):
            yield ''.join(pattern)

# Given hash
given_hash = "91077079768edba10ac0c93b7108bc639d778d67"

# Start time
start_time = time.time()

# Try all patterns
for pattern in generate_patterns():
    if hash_pattern(pattern) == given_hash:
        # Convert the pattern from letters to numbers
        numeric_pattern = [str(ord(char) - ord('a')) for char in pattern]
        time_duration = time.time() - start_time
        print(f"Pattern found: {''.join(numeric_pattern)}")
        print(f"Time taken: {time_duration} seconds")
        break
else:
    print("Pattern not found.")
    print(f"Time taken: {time.time() - start_time} seconds")
