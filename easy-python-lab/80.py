# Problem 80: Right-aligned triangle

n = int(input("Enter number of rows: "))

print("Right-aligned triangle:")
for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * i)
