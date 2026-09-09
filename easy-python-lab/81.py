# Problem 81: Inverted right-aligned triangle

n = int(input("Enter number of rows: "))

print("Inverted right-aligned triangle:")
for i in range(n, 0, -1):
    print(' ' * (n - i) + '*' * i)
