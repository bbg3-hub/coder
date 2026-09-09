# Problem 101: Right-aligned alphabet triangle

n = int(input("Enter number of rows: "))

print("Right-aligned alphabet triangle:")
for i in range(n):
    print(' ' * (n - i - 1), end='')
    for j in range(i + 1):
        print(chr(ord('A') + j), end=' ')
    print()
