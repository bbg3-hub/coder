n = int(input("Enter number of rows: "))

print("Zigzag pattern:")
for i in range(n):
    if i % 2 == 0:
        spaces = i
        print(' ' * spaces + '*')
    else:
        spaces = n - i - 1
        print(' ' * spaces + '*')
