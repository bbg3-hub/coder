char = input("Enter a character: ").lower()

if len(char) == 1:
    if char in 'aeiou':
        print(f"'{char}' is a vowel")
    elif char.isalpha():
        print(f"'{char}' is a consonant")
    else:
        print(f"'{char}' is not an alphabetic character")
else:
    print("Please enter a single character")
