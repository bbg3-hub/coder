n = input("Enter a number: ")

print("Digits from left to right:")
for digit in n:
    if digit != '-':
        print(digit, end=" ")
print()
