# Problem 106: Zigzag pattern

n = int(input("Enter number of rows: "))

print("Zigzag pattern:")
for i in range(n):
    if i % 2 == 0:
        # Left to right
        spaces = i
        print(' ' * spaces + '*')
    else:
        # Right to left
        spaces = n - i - 1
        print(' ' * spaces + '*')
