username = input("Enter username: ")
password = input("Enter password: ")

# Simple validation: correct username and password
valid_username = "admin"
valid_password = "password123"

if username == valid_username and password == valid_password:
    print("Login successful!")
else:
    print("Invalid username or password!")
