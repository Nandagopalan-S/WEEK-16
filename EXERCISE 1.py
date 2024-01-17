"""
WEEK 16
Exercise 1: Password hashing and salting 

"""

# Function to register a username and password
def register_user():
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    print("Registration successful!")
    return username, password

# Function to log in with a username and password
def login_user(username, password):
    entered_username = input("Enter your username: ")
    entered_password = input("Enter your password: ")

    if entered_username == username and entered_password == password:
        print("Login successful!")
        return True
    elif entered_username == username and entered_password != password:
        print("Login failed. Invalid password.")
    elif entered_username != username and entered_password == password:
        print("Login failed. Invalid username.")
    else:
        print("Login failed. Invalid username and password.")
    return False

# Main function
def main():
    username, password = register_user()
    
    # log in with the correct password
    login_user(username, password)

    # log in with a correct username and wrong password
    wrong_password = "wrong_password"
    login_user(username, wrong_password)

    # log in with a wrong username and correct password
    wrong_username = "wrong_user"
    login_user(wrong_username, password)

if __name__ == "__main__":
    main()
