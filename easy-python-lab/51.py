# Problem 51: Check if a number is a palindrome

n = int(input("Enter a number: "))

original = abs(n)
reversed_num = 0
temp = original

while temp > 0:
    digit = temp % 10
    reversed_num = reversed_num * 10 + digit
    temp //= 10

if original == reversed_num:
    print(f"{n} is a palindrome")
else:
    print(f"{n} is not a palindrome")
