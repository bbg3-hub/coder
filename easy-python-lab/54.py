# Problem 54: Extract and print each digit of a number from left to right

n = input("Enter a number: ")

print("Digits from left to right:")
for digit in n:
    if digit != '-':
        print(digit, end=" ")
print()
