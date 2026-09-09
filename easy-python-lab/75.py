# Problem 75: Palindrome Check for string using recursion

def is_palindrome(s):
    # Remove spaces and convert to lowercase
    s = s.replace(" ", "").lower()
    
    if len(s) <= 1:
        return True
    
    if s[0] != s[-1]:
        return False
    
    return is_palindrome(s[1:-1])

string = input("Enter a string: ")

if is_palindrome(string):
    print(f"'{string}' is a palindrome")
else:
    print(f"'{string}' is not a palindrome")
