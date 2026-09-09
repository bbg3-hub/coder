# Problem 35: Check if character is alphabet, digit, or special character

char = input("Enter a single character: ")

if char.isalpha():
    print(f"'{char}' is an alphabet")
elif char.isdigit():
    print(f"'{char}' is a digit")
else:
    print(f"'{char}' is a special character")
